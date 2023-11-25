import calendar
import io
import json
import os
import pathlib
import time

import FlowDataClass
import parameters
import utils

import RPi.GPIO as GPIO
import time, sys, datetime


GPIO.setmode(GPIO.BCM)
GPIO.setup(parameters.FLOW_SENSOR_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

global count, _continue, total_pulse
'''
    count -> will be used to count the pulses
    _continue -> will be used to check the cycle as long as the pulses continue
    total_pulse -> will be used to keep track of the number of pulses in a pouring
'''
count = 0
_continue = 0
total_pulse = 0


def countPulse(channel):
    global count
    if start_counter == 1:
        count = count + 1

GPIO.add_event_detect(parameters.FLOW_SENSOR_GPIO, GPIO.FALLING, callback=countPulse)


def startup():
    print("Please wait while the application is starting up...")
    pathlib.Path(parameters.EXPANDED_PATH).mkdir(parents=True, exist_ok=True)
    if os.path.isfile(parameters.EXPANDED_FILE_NAME_PATH) and os.access(parameters.EXPANDED_FILE_NAME_PATH, os.R_OK):
        # checks if file exists
        print("File exists and is readable.")
    else:
        print("Either file is missing or is not readable, creating file...")
        with io.open(os.path.join(parameters.EXPANDED_PATH, parameters.FILE_NAME), 'w') as db_file:
            # Create a file with empty json array
            db_file.write(json.dumps([]))
    return parameters.START_UP_PARAMETERS_NO_ERROR


if startup() == parameters.START_UP_PARAMETERS_NO_ERROR:
    # Start of infinite loop
    while True:
        try:
            start_counter = 1
            time.sleep(parameters.PULSE_COLLECTION_INTERVAL)
            start_counter = 0

            '''
                seni cok seviyorum BABA!
    
                My 8-year-old daughter wrote this line for
                me while I was away from the computer. So,
                I wanted to send this line to the repository ;)
                It means "I love you so much DAD" in Turkish <3
            '''

            timestamp = calendar.timegm(time.gmtime())
            current_datetime = time.strftime(parameters.current_datetime_format, time.gmtime(timestamp))

            if count != 0:
                total_pulse += count
                # A flow data will be written to the json file for each batch pulse accumulated for half a second.
                print("The pulse is: %.d" % count)
                print(datetime.datetime.utcnow())

                # Start of preparing flow data routine
                flow_data_class = FlowDataClass.FlowData(utils.get_serial_number(), count, 0, 0, 0, timestamp, current_datetime)
                flow_data_str = json.dumps(flow_data_class.__dict__).replace("\\", "")
                utils.write_flow_data_to_disc(flow_data_str)
                # End of preparing flow data routine

                _continue = 1
            else:
                if _continue == 1:
                    # When the flow is completed, it should also be written the batch pulse.
                    print("total pulse: %.d" % total_pulse)
                    print("----------------------")

                    # Start of preparing flow data routine
                    flow_data_class = FlowDataClass.FlowData(utils.get_serial_number(), total_pulse, 1, 1, 1, timestamp, current_datetime)
                    flow_data_str = json.dumps(flow_data_class.__dict__).replace("\\", "")
                    utils.write_flow_data_to_disc(flow_data_str)
                    # End of preparing flow data routine

                    _continue = 0
                    total_pulse = 0

            count = 0
        except KeyboardInterrupt:
            print('\nKeyboard Interrupt! Application stopped by the User.')
            GPIO.cleanup()
            sys.exit()

    # End of infinite loop
else:
    print('Something went wrong...')
