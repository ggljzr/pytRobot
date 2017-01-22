from picamera import PiCamera

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
	pass