import os
import json
import requests

from config import REQUEST_HEADERS, COWIN_DISTRICT_BASE_API, COWIN_STATE_API, STATE_META_FILE_NAME, DISTRICT_META_FILE_NAME, DATA_FOLDER


def get_states():
    response = requests.get(COWIN_STATE_API, headers=REQUEST_HEADERS)
    states = response.json()
    with open(STATE_META_FILE_NAME, 'w') as outfile:
        json.dump(states, outfile, indent=2)


def get_districts():
    if os.path.exists(STATE_META_FILE_NAME):
        with open(STATE_META_FILE_NAME, 'r') as infile:
            states_meta = json.load(infile)
    states = states_meta['states']
    state_district_map = []
    for state in states:
        url = COWIN_DISTRICT_BASE_API.format(state['state_id'])
        response = requests.get(url, headers=REQUEST_HEADERS)
        state_district_map += response.json()["districts"]

    with open(DISTRICT_META_FILE_NAME, 'w') as outfile:
        json.dump(state_district_map, outfile, indent=2)


if os.path.exists(STATE_META_FILE_NAME):
    os.remove(STATE_META_FILE_NAME)

if os.path.exists(DISTRICT_META_FILE_NAME):
    os.remove(DISTRICT_META_FILE_NAME)

if not os.path.exists(DATA_FOLDER):
    os.mkdir(DATA_FOLDER)

get_states()
get_districts()
