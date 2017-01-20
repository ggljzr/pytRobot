import pytrobot.camera as camera
import os.path
import subprocess as sb

def test_create_img():
	path = 'test_img.jpg'
	sb.run(['rm', '-f', path])
	camera.capture_img(img_path=path)
	assert os.path.isfile(path)
	sb.run(['rm', '-f', path])
