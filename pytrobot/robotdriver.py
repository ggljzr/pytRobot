import RPi.GPIO as GPIO
import time

class DirError(Exception):
    def __init__(self, direction):
        self.message = '{} is not valid direction, has to be left/right/forward'.format(direction)

class RobotDriver:
    """
    **Class for accessing robot motors and camera**
    """

    def __init__(self, left_motor_pin = 4, right_motor_pin = 7):
        """
        Pin mode is set to BCM.
        """

        self.left_motor_pin = left_motor_pin
        self.right_motor_pin = right_motor_pin
    
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.left_motor_pin, GPIO.OUT)
        GPIO.setup(self.right_motor_pin, GPIO.OUT)
            
    def stop(self):
        """
        Sets both motor pins LOW.
        """

        GPIO.output(self.left_motor_pin, GPIO.LOW)
        GPIO.output(self.right_motor_pin, GPIO.LOW)

    def forward(self, period=0.5):
        """
        Moves robot forward (sets both motor pins HIGH).

        ``period`` ( = 0.5) -- period for which are motors active (seconds)
        """

        print('ROBOT: Going forward for {} seconds'.format(period))
        GPIO.output(self.left_motor_pin, GPIO.HIGH)
        GPIO.output(self.right_motor_pin, GPIO.HIGH)

        time.sleep(period)
        self.stop()

    def left(self, period=0.5):
        """
        Turns robot left (sets right motor pin HIGH).

        ``period`` ( = 0.5) -- period for which is right motor active (seconds)
        """

        print('ROBOT: Turning left for {} seconds'.format(period))
        GPIO.output(self.left_motor_pin, GPIO.HIGH)

        time.sleep(period)
        self.stop()

    def right(self, period=0.5):
        """
        Turns robot right (sets left motor pin HIGH).

        ``period`` ( = 0.5) -- period for which is left motor active (seconds)
        """

        print('ROBOT: Turning right for {} seconds'.format(period))
        GPIO.output(self.right_motor_pin, GPIO.HIGH)

        time.sleep(period)
        self.stop()

    def move(self, direction, period=0.5):
        """
        Moves robot in given direction.

        ``direction`` -- left/right/forward (string)
        ``period`` ( = 0.5) -- period for which are motors active (seconds)

        Raises ``DirError`` in case direction is not left/right/forward.
        """

        if direction == 'forward':
            self.forward(period)
        elif direction == 'left':
            self.left(period)
        elif direction == 'right':
            self.right(period)
        else:
            raise DirError(direction)

    def cleanup(self):
        """
        Calls GPIO.cleanup().
        """

        GPIO.cleanup()

