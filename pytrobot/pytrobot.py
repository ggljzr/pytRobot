import click
from .robotdriver import RobotDriver, DirError
from .camera import RobotCamera

@click.group()
def main():
    pass

@main.group()
def console():
    pass

@console.command()
def capture():
	camera = RobotCamera()
	camera.capture_img()
	camera.camera.close()

@console.command()
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

@console.command()
@click.option('--period', '-p',
			  help='Motor activation period (seconds)',
			  default=0.5)
def forward(period):
	robot = RobotDriver()
	robot.forward(period)
	robot.cleanup()

@main.command()
def web():
	from .flaskapp import app

	app.robot = RobotDriver()
	app.run(host='raspberrypi.local', debug=True)
