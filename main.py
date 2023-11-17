import io
import json
import os

'''
id|pulse|ml|factor|milliliter|cl|timestamp
'''

START_UP_PARAMETERS_NO_ERROR = 0
START_UP_PARAMETERS_ERROR = 1

PATH = '/projects/wdspy-raspi/'
FILE_NAME = 'pourings.json'
FULL_PATH = PATH + FILE_NAME


def startup():
    print("Please wait while the application is starting up...")
    if os.path.isfile(FULL_PATH) and os.access(FULL_PATH, os.R_OK):
        # checks if file exists
        print("File exists and is readable.")
    else:
        print("Either file is missing or is not readable, creating file...")
        with io.open(os.path.join(PATH, FILE_NAME), 'w') as db_file:
            db_file.write(json.dumps([]))
    return START_UP_PARAMETERS_NO_ERROR


def write_file(pouring):
    with open(FULL_PATH) as fp:
        pourings = json.load(fp)

    pourings.append(pouring)

    with open(FULL_PATH, 'w') as json_file:
        json.dump(pourings, json_file, indent=2, separators=(',', ': '))


if startup() == START_UP_PARAMETERS_NO_ERROR:
    pouring = {"a": 54, "b": 87}
    write_file(pouring)
else:
    print('Something went wrong...')
