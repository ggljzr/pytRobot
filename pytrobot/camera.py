from picamera import PiCamera

def capture_img(img_path='img.jpg', res=(1024,768), vflip=True):
	"""
	Captures image with PiCamera and saves it to given path.
	"""

	camera = PiCamera()
	camera.resolution = res
	camera.vflip = vflip

	print('CAMERA: Capturing image...')
	camera.capture(img_path)
	print('CAMERA: Image saved in {}'.format(img_path))

	camera.close()

def start_stream(res=(640,480), vflip=True):
	"""
	Starts mjpg-streamer process.
	"""

	pass

def stop_stream():
	"""
	Stops mjpg-streamer process.
	"""

	pass

