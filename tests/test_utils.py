import pytest

import pytrobot.utils as utils

def test_handled_float():
	val = utils.handled_float('123.456')
	assert val == 123.456
	val = utils.handled_float(value=None, default=42.0)
	assert val == 42.0
	val = utils.handled_float('not so floaty float', default=42.0)
	assert val == 42.0
	val = utils.handled_float('not so inty int', default=None)
	assert val == None

def test_get_interfaces():
	interfaces = utils.get_interfaces()

	assert 'lo' in interfaces
	assert 'ip' in interfaces['lo']
	assert 'hwaddr' in interfaces['lo']

def test_sysinfo():
	info = utils.sys_info()

	assert 'interfaces' in info
	assert 'nodename' in info