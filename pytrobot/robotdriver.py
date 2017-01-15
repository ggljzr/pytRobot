import RPi.GPIO as GPIO

class RobotDriver:
    def __init__(self, left_motor_pin = 4, right_motor_pin = 7):
        self.left_motor_pin = left_motor_pin
        self.right_motor_pin = right_motor_pin
    
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.left_motor_pin, GPIO.OUTPUT)
        GPIO.setup(self.right_motor_pin, GPIO.OUTPUT)
            
    def stop(self):
        GPIO.output(self.left_motor_pin, GPIO.LOW)
        GPIO.output(self.right_motor_pin, GPIO.LOW)

    def forward(self):
        GPIO.output(self.left_motor_pin, GPIO.HIGH)
        GPIO.output(self.left_motor_pin, GPIO.HIGH)

    def left(self):
        GPIO.output(self.left_motor_pin, GPIO.HIGH)

    def right(self):
        GPIO.output(self.right_motor_pin, GPIO.HIGH)

    def cleanup(self):
        GPIO.cleanup()
