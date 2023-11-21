import RPi.GPIO as GPIO
import parameters

FLOW_SENSOR_GPIO = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(parameters.FLOW_SENSOR_GPIO, GPIO.IN, pull_up_down = GPIO.PUD_UP)

global count
count = 0

def countPulse(channel)
    # Write the method to collect the number of pulses here


GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=countPulse)