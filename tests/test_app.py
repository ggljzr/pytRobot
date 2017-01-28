import pytest
import json

from pytrobot.robotdriver import RobotDriver, DirError

@pytest.fixture
def testapp():
	from pytrobot.flaskapp import app
	app.robot = RobotDriver()
	app.streamer = None
	app.is_stream = False

	return app.test_client()

def test_index(testapp):
	assert 'pytRobot' in testapp.get('/').data.decode('utf-8')

def test_no_stream(testapp):
	assert 'nostream' in testapp.get('/').data.decode('utf-8')

def test_info_json(testapp):
	info_data = testapp.get('/info').data.decode('utf-8')
	info_data = json.loads(info_data)

	assert 'interfaces' in info_data
	assert 'nodename' in info_data

	assert 'lo' in info_data['interfaces']
