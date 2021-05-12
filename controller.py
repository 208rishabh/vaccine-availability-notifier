from config import notification_details, DISTRICT_META_FILE_NAME
import data
import telegram_notifier
import os
import json

m = "\nDate: {}\n\n* {} \n"
prefix_vaccine = "Vaccine: {}\n"
prefix_age = "Min Age: {}\n"
prefix_district = "District: {}\n"


def format_message(message, detail):
    response = ''
    districts = []
    if os.path.exists(DISTRICT_META_FILE_NAME):
        with open(DISTRICT_META_FILE_NAME, 'r') as infile:
            districts = json.load(infile)
    for district in districts:
        if district['district_id'] == detail['district_id']:
            response += prefix_district.format(district['district_name'])
            continue

    if 'min_age' in detail.keys():
        response += prefix_age.format(detail['min_age'])
    if 'vaccine_type' in detail.keys():
        response += prefix_vaccine.format(detail['vaccine_type'])
    keys = sorted(message.keys())
    for item in keys:
        response += m.format(item, "\n* ".join(message[item]))
    return response


for item in notification_details:
    centres = data.fetch_data(item['district_id'], False)
    valid_centres = {}
    for centre in centres:
        if len(centre['sessions']) == 0:
            continue
        valid_sessions = [session for session in centre['sessions']]
        for session in centre['sessions']:
            if session['available_capacity'] < 1:
                valid_sessions.remove(session)
            elif 'vaccine_type' in item.keys() and session['vaccine'] != item['vaccine_type']:
                valid_sessions.remove(session)
            elif 'min_age' in item.keys() and session['min_age_limit'] != item['min_age']:
                valid_sessions.remove(session)
        for session in valid_sessions:
            if not session['date'] in valid_centres.keys():
                valid_centres[session['date']] = []
            valid_centres[session['date']].append(centre['name'])
    if 'chat_id' in item.keys() and len(valid_centres) > 0:
        telegram_notifier.send_message(item['chat_id'], format_message(valid_centres, item))

