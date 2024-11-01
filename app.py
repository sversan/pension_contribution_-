import RPi.GPIO as GPIO
import time

# Setup GPIO pins
LEFT_WHEEL_FORWARD = 17
LEFT_WHEEL_BACKWARD = 18
RIGHT_WHEEL_FORWARD = 22
RIGHT_WHEEL_BACKWARD = 23

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)

# Set all pins as output
GPIO.setup(LEFT_WHEEL_FORWARD, GPIO.OUT) #Make LEft Suddenly
GPIO.setup(LEFT_WHEEL_BACKWARD, GPIO.OUT)
GPIO.setup(RIGHT_WHEEL_FORWARD, GPIO.OUT)
GPIO.setup(RIGHT_WHEEL_BACKWARD, GPIO.OUT)

def turn_right_fast():
    # Stop left wheel
    GPIO.output(LEFT_WHEEL_FORWARD, GPIO.LOW)
    GPIO.output(LEFT_WHEEL_BACKWARD, GPIO.LOW)

    # Spin right wheel forward quickly
    GPIO.output(RIGHT_WHEEL_FORWARD, GPIO.HIGH)
    GPIO.output(RIGHT_WHEEL_BACKWARD, GPIO.LOW)

    time.sleep(1)  # Adjust time for how long to turn right

    # Stop right wheel after the turn
    GPIO.output(RIGHT_WHEEL_FORWARD, GPIO.LOW)
    GPIO.output(RIGHT_WHEEL_BACKWARD, GPIO.LOW)

try:
    turn_right_fast()
finally:
    GPIO.cleanup()  # Clean up GPIO pins
