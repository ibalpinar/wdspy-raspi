import parameters
import os
import io
import json
import pathlib

'''
pulse|ml|factor|milliliter|cl|timestamp
'''


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


def write_file(pouring):
    with open(parameters.EXPANDED_FILE_NAME_PATH) as fp:
        pourings = json.load(fp)

    pourings.append(pouring)

    with open(parameters.EXPANDED_FILE_NAME_PATH, 'w') as json_file:
        json.dump(pourings, json_file, indent=2, separators=(',', ': '))


if startup() == parameters.START_UP_PARAMETERS_NO_ERROR:
    pouring = {"a": 54, "b": 87}
    write_file(pouring)
else:
    print('Something went wrong...')
