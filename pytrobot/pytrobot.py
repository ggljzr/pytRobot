import click

from .robotdriver import RobotDriver, DirError
from .camera import RobotCamera
from .utils import print_info

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
	camera = RobotCamera()
	camera.capture_img(file)
	camera.camera.close()

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
def web():
	from .flaskapp import app

	app.robot = RobotDriver()
	app.run(host='raspberrypi.local', debug=True)
	app.robot.cleanup()
