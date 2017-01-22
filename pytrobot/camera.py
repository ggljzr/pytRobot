from picamera import PiCamera
import subprocess as sb
import os

def capture_img(img_path='img.jpg', res=(1024,768), vflip=True):
	"""
	Captures image with PiCamera and saves it to given path.
	It cannot be used when camera is active 
	(for example when it is used by mjpg-streamer). In that case
	exception ``PiCameraMMALError`` will be raised.
	"""
	camera = PiCamera()

	camera.resolution = res
	camera.vflip = vflip

	print('CAMERA: Capturing image...')
	camera.capture(img_path)
	print('CAMERA: Image saved in {}'.format(img_path))

	camera.close()

class MjpgStreamer:
	"""
	**Interface for controlling mjpg-streamer process**
	"""

	def __init__(self, path, resolution=(640, 480), fps=25):
		self.resolution = resolution
		self.fps = fps
		self.path = path
		self.stream_process = None

	def start_stream(self):

		input_str = 'input_raspicam.so -x {} -y {} -fps {} -vf'.format(self.resolution[0], self.resolution[1], self.fps)
		output_str = 'output_http.so -w {}/www'.format(self.path)

		plugin_env = os.environ.copy()
		plugin_env['LD_LIBRARY_PATH'] = self.path

		print('STREAMER: Starting stream...')
		self.stream_process = sb.Popen([self.path + '/mjpg_streamer', 
									'-o', output_str,
									'-i', input_str], env=plugin_env)
		print('STREAMER: Process running with PID {}'.format(self.stream_process.pid))

	def stop_stream(self):
		print('STREAMER: Terminating mjpg_streamer process')
		self.stream_process.kill()