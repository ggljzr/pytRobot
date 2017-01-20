import pytest

from pytrobot.robotdriver import RobotDriver, DirError

def test_dir_exception():
	robot = RobotDriver()
	with pytest.raises(DirError):
		robot.move(direction='not so lefty left')

	robot.move(direction='left')