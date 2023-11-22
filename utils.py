import json
import parameters


def write_flow_data_to_disc(flow_data):
    with open(parameters.EXPANDED_FILE_NAME_PATH) as fp:
        pourings = json.load(fp)

    pourings.append(json.loads(flow_data))

    with open(parameters.EXPANDED_FILE_NAME_PATH, 'w') as json_file:
        json.dump(pourings, json_file, indent=2, separators=(',', ': '))


def get_serial_number():
    # extract serial from cpuinfo file
    cpu_serial_number = "0000000000000000"
    try:
        f = open('/proc/cpuinfo', 'r')
        for line in f:
            if line[0:6] == 'Serial':
                cpu_serial_number = line[10:26]
        f.close()
    except AttributeError:
        cpu_serial_number = "ERROR000000000"

    return cpu_serial_number
