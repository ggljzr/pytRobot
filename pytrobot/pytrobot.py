import click
from .robotdriver import RobotDriver, DirError

robot = RobotDriver()

@click.group()
def main():
    robot.cleanup()

@main.group()
def console():
    robot.cleanup()

@console.command()
def capture():
    robot.capture_img()
    robot.cleanup()

@console.command()
@click.argument('direction')
@click.option('--period', '-p',
			  help='Motor activation period (seconds)', 
			  default=0.5)
def turn(direction, period):
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
    robot.forward(period)
    robot.cleanup()

@console.command()
def cleanup():
	robot.cleanup()

@main.command()
def web():
    print('hello www!!!!')
    robot.cleanup()
