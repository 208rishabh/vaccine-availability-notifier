import requests
from datetime import date
import json
import os
from config import REQUEST_HEADERS, VACCINE_TRACKER_BASE_URL
import logging

CENTRE_FILE_NAME = "./centre-{}.json"


def fetch_data(district_id, persist_in_file):
    file_name= CENTRE_FILE_NAME.format(district_id)
    if os.path.exists(file_name):
        os.remove(file_name)
    d = date.today().strftime("%d-%m-%y")
    API_URL = VACCINE_TRACKER_BASE_URL.format(district_id, d)
    response = requests.get(API_URL, headers=REQUEST_HEADERS)
    centre_list = []
    if response.status_code != 200:
        logging.error("No response from Cowin")
        return centre_list
    centre_list = response.json()['centers']
    if persist_in_file:
        with open(file_name.format(district_id), 'w') as outfile:
            json.dump(centre_list, outfile, indent=2)
    return centre_list
