import click
from picamera.exc import PiCameraMMALError

from .robotdriver import RobotDriver, DirError
from .camera import capture_img, MjpgStreamer
from .utils import print_info, parse_config, DEFAULT_CONFIG

@click.group()
def main():
    pass

@main.group(help='Control robot via console commands')
def console():
    pass

@console.command(help='Captures image with PiCamera')
@click.option('--file', '-f',
			help='Output file (default img.jpg)',
			default='img.jpg')
def capture(file):
	try:
		capture_img(img_path=file)
	except PiCameraMMALError as e:
		print('Failed to alocate camera resources.')
		print('Perhaps camera is used by mjpg-streamer.')
		print('PiCameraMMALError message:')
		print(str(e))

@console.command(help='Makes a turn in given direction (left/right)')
@click.argument('direction')
@click.option('--period', '-p',
			  help='Motor activation period (seconds)', 
			  default=0.5)
def turn(direction, period):
	robot = RobotDriver()
	try:
		robot.move(direction, period)
	except DirError as e:
		print(e.message)

	robot.cleanup()

@console.command(help='Goes forward')
@click.option('--period', '-p',
			  help='Motor activation period (seconds)',
			  default=0.5)
def forward(period):
	robot = RobotDriver()
	robot.forward(period)
	robot.cleanup()

@console.command(help='Shows system info')
def info():
	print_info()

@main.command(help='Runs embedded flask server with web interface')
@click.option('--config', '-c',
			help='/path/to/config/file.ini',
			default=DEFAULT_CONFIG)
def web(config):
	from .flaskapp import app

	print('Starting web app...')
	print('Config: {}'.format(config))
	cfg = parse_config(config)

	app.robot = RobotDriver()
	app.streamer = MjpgStreamer(path=cfg['streamer']['path'])
	app.run(host='raspberrypi.local', debug=True)
	app.robot.cleanup()
	app.streamer.stop_stream()
