REQUEST_HEADERS = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}
TELEGRAM_BOT_SEND_MESSAGE_API = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
COWIN_STATE_API = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
COWIN_DISTRICT_BASE_API = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}"
VACCINE_TRACKER_BASE_URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}"
DATA_FOLDER = "./data"
STATE_META_FILE_NAME = DATA_FOLDER + "/state.json"
DISTRICT_META_FILE_NAME = DATA_FOLDER + "/district.json"
COVAXIN = "COVAXIN"
COVISHIELD = "COVISHIELD"


notification_details = [
    {
        'state_id': 4,
        'district_id': 49,
        'chat_id': '-1001448650253',
        'vaccine_type': COVAXIN,
        'min_age': 45
    },
    {
        'state_id': 4,
        'district_id': 45,
        'chat_id': '-1001448650253',
        'min_age': 18
    }
]