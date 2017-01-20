import RPi.GPIO as GPIO
import time
from picamera import PiCamera

class DirError(Exception):
    def __init__(self, direction):
        self.message = '{} is not valid direction, has to be left/right/forward'.format(direction)

class RobotDriver:
    def __init__(self, left_motor_pin = 4, right_motor_pin = 7):
        self.left_motor_pin = left_motor_pin
        self.right_motor_pin = right_motor_pin
    
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.left_motor_pin, GPIO.OUT)
        GPIO.setup(self.right_motor_pin, GPIO.OUT)

        self.camera = PiCamera()
        self.camera.resolution = (1024, 768)
        self.camera.start_preview()
        self.camera.vflip = True
        self.camera_warmup = True
            
    def stop(self):
        GPIO.output(self.left_motor_pin, GPIO.LOW)
        GPIO.output(self.right_motor_pin, GPIO.LOW)

    def forward(self, period=0.5):
        print('ROBOT: Going forward for {} seconds'.format(period))
        GPIO.output(self.left_motor_pin, GPIO.HIGH)
        GPIO.output(self.left_motor_pin, GPIO.HIGH)

        time.sleep(period)
        self.stop()

    def left(self, period=0.5):
        print('ROBOT: Turning left for {} seconds'.format(period))
        GPIO.output(self.left_motor_pin, GPIO.HIGH)

        time.sleep(period)
        self.stop()

    def right(self, period=0.5):
        print('ROBOT: Turning right for {} seconds'.format(period))
        GPIO.output(self.right_motor_pin, GPIO.HIGH)

        time.sleep(period)
        self.stop()

    def move(self, direction, period=0.5):
        if direction == 'forward':
            self.forward(period)
        elif direction == 'left':
            self.left(period)
        elif direction == 'right':
            self.right(period)
        else:
            raise DirError(direction)

    def cleanup(self):
        GPIO.cleanup()
        self.camera.close()

    def capture_img(self, img_path='img.jpg'):
        if self.camera_warmup:
            time.sleep(2)
            self.camera_warmup = False

        print('Capturing image...')
        self.camera.capture(img_path)
        print('Image saved in {}'.format(img_path))



