import netifaces as nif
import subprocess as sb
import os
import click
import configparser

DEFAULT_CONFIG = '/etc/xdg/pytrobot/config.ini'

def parse_config(config_path=DEFAULT_CONFIG):
	cfg = configparser.ConfigParser()
	cfg.read(config_path)

	try:
		streamer_path = cfg['streamer']['path']
		resx = cfg['streamer']['resx']
		resy = cfg['streamer']['resy']
		fps = cfg['streamer']['fps']
	except KeyError as e:
		print('Config file is missing or containing errors.')
		if config_path == DEFAULT_CONFIG:
			print('Default config file should be placed in {}.'.format(DEFAULT_CONFIG))
			print('Alternatively you could use -c/--config option to specify custom config file.')
		print('KeyError message:')
		raise e

	return {'path' : streamer_path, 'resx' : resx, 'resy' : resy, 'fps' : fps}


def handled_float(value, default=0):
	"""
	Returns ``float(value)`` if value is parseable by ``float()``.
	Otherwise returns ``default``. 
	"""
	ret_val = default

	try:
		ret_val = float(value)
	except (TypeError, ValueError):
		pass

	return ret_val

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

		new_interface['hwaddr'] = addrs[nif.AF_LINK][0]['addr']

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
	for key, value in info['interfaces'].items():
		click.echo(key)
		click.echo('	Address: {}'.format(value['ip']))
		click.echo('	HW address: {}'.format(value['hwaddr']))
