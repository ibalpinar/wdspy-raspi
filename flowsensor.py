#!/usr/bin/python
import RPi.GPIO as GPIO
import time, sys
from datetime import datetime
 
FLOW_SENSOR_GPIO = 13
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR_GPIO, GPIO.IN, pull_up_down = GPIO.PUD_UP)
 
global count, _continue, total_pulse
count = 0
_continue = 0
total_pulse = 0
 
def countPulse(channel):
   global count
   if start_counter == 1:
      count = count+1
 
GPIO.add_event_detect(FLOW_SENSOR_GPIO, GPIO.FALLING, callback=countPulse)
 
while True:
    try:
        start_counter = 1
        time.sleep(0.5)
        start_counter = 0
        
        '''
            seni cok seviyorum BABA!
            
            My 8-year-old daughter wrote this line for
            me while I was away from the computer. So,
            I wanted to send this line to the repository ;)
            It means "I love you so much DAD" in Turkish <3
        '''

        if count != 0:
            total_pulse += count
            # A flow data will be written to the json file for each batch pulse accumulated for half a second.
            print("The pulse is: %.d" %(count))
            print(datetime.utcnow())
            _continue = 1
        else:
            if _continue == 1:
                # When the flow is completed, it should also be written the batch pulse.
                print("total pulse: %.d" %(total_pulse))
                print("----------------------")
                _continue = 0
                total_pulse = 0
                
        count = 0
    except KeyboardInterrupt:
        print('\nkeyboard interrupt!')
        GPIO.cleanup()
        sys.exit()
