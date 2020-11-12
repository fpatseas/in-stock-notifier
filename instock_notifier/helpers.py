import os
import json

import config
import utils

from datetime import date, datetime

def notify(url):
    try:
        utils.send_email(
            config.EMAIL_SENDER,
            config.EMAIL_RECIPIENTS,
            "In-Stock Product",
            "<a href='"+ url +"' target='_blank'>"+ url +"</a>")

        print('Email sent!')
    except Exception as e:
        print(e)
			
def must_notify(url):
    try:
        file = "notifications.json"
        jsonFile = open(file, "r")

        if os.path.getsize(file) > 0:
            data = json.load(jsonFile)
        else:
            data = { "notifications": [] }

        jsonFile.close()

        notifications = data["notifications"]

        if len(notifications) > 0:
            send = True
            found = False
			
            for notification in notifications:
                if notification["url"] == url:
                    found = True

                    lastsent = datetime.strptime(notification["lastsent"], r"%Y-%m-%dT%H:%M:%S.%f")
                    diff_in_seconds = (datetime.now() - lastsent).total_seconds()
                    diff_in_minutes = divmod(diff_in_seconds, 60)[0]
                    diff_in_hours = divmod(diff_in_seconds, 3600)[0]

                    if diff_in_hours > config.RESEND_AFTER_INHOURS:
                        notification["lastsent"] = datetime.now()
                    else:
                        send = False
						
            if found == False:
                notifications.append({ "url": url, "lastsent": datetime.now() })
        else:
            notifications.append({ "url": url, "lastsent": datetime.now() })
			
        jsonFile = open("notifications.json", "w+")
        jsonFile.write(json.dumps(data, indent=4, default=utils.json_serial))
        jsonFile.close()
    except Exception as e:
        print(e)

    if send == False:
        print('Email already sent')
		
    return send