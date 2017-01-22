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
		"""
		``path`` -- path to mjpg-streamer location. 
		For example '/home/pi/mjpg-streamer'.
		"""

		self.resolution = resolution
		self.fps = fps
		self.path = path
		self.stream_process = None

	def start_stream(self):
		"""
		Starts streaming process. Stream is served via 
		web server (port 8080).

		If there was previous streaming process 
		created with this method, it will be terminated.
		"""

		if self.stream_process is not None:
			print("STREAMER: Killing previous stream (PID: {})".format(self.stream_process.pid))
			self.stream_process.kill()

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
		"""
		Kills created streaming process. 
		Does nothing when no known stream process exists.
		"""

		if self.stream_process is None:
			print('STREAMER: No streaming process is running with this instance.')
			return

		print('STREAMER: Terminating mjpg_streamer process')
		self.stream_process.kill()
		self.stream_process = None