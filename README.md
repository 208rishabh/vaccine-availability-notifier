# vaccine-availability-notifier

For any given district, get notified on a telegram channel when covid vaccine is available. The notifications are configurable for certain vaccine types or age groups as well. Different telegram channels can be notified for different use case (district - vaccine - age group combinations). Vaccine type and age groups are not mandatory parameters.

How to setup?
* Get a telegram bot and set the token as env called `TELEGRAM_BOT_TOKEN`.
* Configure the criteria for which notifications need to be sent out in `config.py`. Execute `meta.py` to get district id and state id.
* Create channels on telegram and add the bot as admin. Use channel id in `config.py`. Same or different channels can be used for notifying different use cases.
* Check the frequency in `scheduler.py` and adjust as per the need. If the demand is not very high, dont use an aggresive cron.
* Execute `scheduler.py`.
