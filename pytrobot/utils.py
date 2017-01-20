import netifaces as nif
import subprocess as sb
import os
import click

def get_interfaces():
	"""
	Return list of dicts with available network interfaces and their addresses.
	"""

	interfaces = []

	for interface in nif.interfaces():
		new_interface = {}
		new_interface['name'] = interface

		addrs = nif.ifaddresses(interface)

		try:
			new_interface['ip'] = addrs[nif.AF_INET][0]['addr']
		except KeyError:
			new_interface['ip'] = 'None'

		new_interface['hwaddr'] = addrs[nif.AF_LINK][0]['addr']

		interfaces.append(new_interface)

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

def print_info():
	"""
	Prints formated and colored system info to stdout.
	"""

	info = sys_info()

	click.secho('---System Info---', fg='cyan')
	click.echo('Nodename: {}'.format(info['nodename']))
	click.echo('OS: {}, (kernel: {})'.format(info['os'], info['kernel']))
	click.echo('Uptime: {}'.format(info['uptime']))

	click.secho('---Interfaces---', fg='yellow')
	for interface in info['interfaces']:
		click.echo(interface['name'])
		click.echo('	Address: {}'.format(interface['ip']))
		click.echo('	HW address: {}'.format(interface['hwaddr']))
