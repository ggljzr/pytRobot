import pytest

import pytrobot.utils as utils

def test_get_interfaces():
	interfaces = utils.get_interfaces()

	assert 'lo' in interfaces
	assert 'ip' in interfaces['lo']
	assert 'hwaddr' in interfaces['lo']

def test_sysinfo():
	info = utils.sys_info()

	assert 'interfaces' in info
	assert 'nodename' in info