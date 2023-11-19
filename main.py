import io
import json
import os
import pathlib
import datetime

'''
pulse|ml|factor|milliliter|cl|timestamp
'''

current_date = datetime.date.today().strftime('%Y%m%d')
START_UP_PARAMETERS_NO_ERROR = 0
START_UP_PARAMETERS_ERROR = 1
PATH = '~/Projects/wdspy-raspi-data/'
FILE_NAME = 'pourings-' + current_date + '.json'
FULL_PATH = PATH + FILE_NAME
EXPANDED_PATH = os.path.expanduser(PATH)
EXPANDED_FILE_NAME_PATH = os.path.expanduser(FULL_PATH)


def startup():
    print("Please wait while the application is starting up...")
    pathlib.Path(EXPANDED_PATH).mkdir(parents=True, exist_ok=True)
    if os.path.isfile(EXPANDED_FILE_NAME_PATH) and os.access(EXPANDED_FILE_NAME_PATH, os.R_OK):
        # checks if file exists
        print("File exists and is readable.")
    else:
        print("Either file is missing or is not readable, creating file...")
        with io.open(os.path.join(EXPANDED_PATH, FILE_NAME), 'w') as db_file:
            # Create a file with empty json array
            db_file.write(json.dumps([]))
    return START_UP_PARAMETERS_NO_ERROR


def write_file(pouring):
    with open(EXPANDED_FILE_NAME_PATH) as fp:
        pourings = json.load(fp)

    pourings.append(pouring)

    with open(EXPANDED_FILE_NAME_PATH, 'w') as json_file:
        json.dump(pourings, json_file, indent=2, separators=(',', ': '))


if startup() == START_UP_PARAMETERS_NO_ERROR:
    pouring = {"a": 54, "b": 87}
    write_file(pouring)
else:
    print('Something went wrong...')
