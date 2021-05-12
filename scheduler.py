import time
import schedule
from controller import run
from meta import refresh_meta
from datetime import datetime
import logging
logging.basicConfig(level=logging.INFO)


def get_time(identifier):
    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    logging.info("Running %s at %s", identifier, time)
    return time


def cron_notif():
    time = get_time("notification")
    run()
    get_time(time)


def cron_meta():
    time = get_time("meta")
    refresh_meta()
    get_time(time)


schedule.every(9).seconds.do(cron_notif)
schedule.every().day.at("05:30").do(cron_meta)

while True:
    schedule.run_pending()
    time.sleep(1)