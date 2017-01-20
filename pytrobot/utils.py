import netifaces as nif
import subprocess as sb
import os

def get_interfaces():
	"""
	Return dict with available network interfaces and their addresses.
	"""

	interfaces = {}

	for interface in nif.interfaces():
		new_interface = {}
		new_interface['name'] = interface

		addrs = nif.ifaddresses(interface)

		try:
			new_interface['ip'] = addrs[nif.AF_INET][0]['addr']
		except KeyError:
			new_interface['ip'] = 'None'

		new_interface['HW address'] = addrs[nif.AF_LINK][0]['addr']

		interfaces[interface] = new_interface

	return interfaces

def get_uptime():
	"""
	Returns system uptime (string).
	"""

	out = str(sb.check_output(['uptime']))
	out = out.replace(',','')

	return out.split()[3]

def sys_info():
	"""
	Returns dict with system information:

	``nodename``

	``os`` -- used operating system

	``kernel`` -- kernel version

	``uptime``

	``interfaces`` -- network interfaces
	
	"""

	info = os.uname()
	return {'nodename' : info.nodename,
			'os' : info.sysname,
			'kernel' : info.release,
			'uptime' : get_uptime(),
			'interfaces' : get_interfaces()}
