import os
import datetime

current_date = datetime.date.today().strftime('%Y%m%d')
START_UP_PARAMETERS_NO_ERROR = 0
START_UP_PARAMETERS_ERROR = 1
PATH = '~/Projects/data/wdspy-raspi-data/'
FILE_NAME = 'pourings-' + current_date + '.json'
FULL_PATH = PATH + FILE_NAME
EXPANDED_PATH = os.path.expanduser(PATH)
EXPANDED_FILE_NAME_PATH = os.path.expanduser(FULL_PATH)

FLOW_SENSOR_GPIO = 13