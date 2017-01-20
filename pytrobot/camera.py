from picamera import PiCamera

class RobotCamera:
	"""
	**Simple interface for PiCamera.**
	"""

	def __init__(self, resolution=(1024,768)):
		self.camera = PiCamera()
		self.camera.resolution = resolution
		self.camera.start_preview()
		self.camera.vflip = True

	def capture_img(self, img_path='img.jpg'):
		print('CAMERA: Capturing image...')
		self.camera.capture(img_path)
		print('CAMERA: Image saved in {}'.format(img_path))

