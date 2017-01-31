import pytest
import json
import imghdr

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
	info_data = testapp.get('/info/').data.decode('utf-8')
	info_data = json.loads(info_data)

	assert 'interfaces' in info_data
	assert 'nodename' in info_data

	assert 'lo' in info_data['interfaces']

def test_move_redirect(testapp):
	req = testapp.get('/move/forward/1/')
	data = req.data.decode('utf-8')

	assert req.status_code == 302

def test_move_invalid(testapp):
	#with implicit value is correct
	req = testapp.get('/move/forward/')
	assert req.status_code == 302

	#invalid direction
	req = testapp.get('/move/alt-righty-right/1/')
	assert req.status_code == 406

	#invalid time period
	req = testapp.get('/move/left/not-floaty-float/')
	assert req.status_code == 406

#this test capture command with capture_img() function
#since no streamer is present
def test_capture(testapp):
	req = testapp.get('/capture/')
	assert req.status_code == 200
	assert imghdr.what(None, h=req.data) == 'jpeg'



