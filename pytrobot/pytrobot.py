import click
from .robotdriver import RobotDriver, DirError

@click.group()
def main():
    pass

@main.group()
def console():
    pass

@console.command()
def capture():
	robot = RobotDriver()
    robot.capture_img()
    robot.cleanup()

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

    app.run(host='raspberrypi.local', debug=True)
