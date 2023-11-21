import calendar
import io
import json
import os
import pathlib
import time

import FlowDataClass
import parameters


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


def write_flow_data_to_disc(flow_data):
    with open(parameters.EXPANDED_FILE_NAME_PATH) as fp:
        pourings = json.load(fp)

    pourings.append(json.loads(flow_data))

    with open(parameters.EXPANDED_FILE_NAME_PATH, 'w') as json_file:
        json.dump(pourings, json_file, indent=2, separators=(',', ': '))


if startup() == parameters.START_UP_PARAMETERS_NO_ERROR:
    timestamp = calendar.timegm(time.gmtime())
    current_datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timestamp))

    flow_data_class = FlowDataClass.FlowData(453, 5, 550, 5, timestamp, current_datetime)
    flow_data_str = json.dumps(flow_data_class.__dict__).replace("\\", "")

    write_flow_data_to_disc(flow_data_str)

else:
    print('Something went wrong...')
