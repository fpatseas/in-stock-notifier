import os
import sys
sys.path.append("../instock_notifier")

import config

from mailjet_rest import Client

mailjet = Client(auth=(config.SMTP_API_KEY, config.SMTP_API_SECRET), version="v3.1")
data = {
    "Messages": [
        {
            "From": config.EMAIL_SENDER,
            "To": config.EMAIL_RECIPIENTS,
            "Subject": "Greetings from Mailjet.",
            "TextPart": "My first Mailjet email",
            "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
            "CustomID": "AppGettingStartedTest"
        }
    ]
}
result = mailjet.send.create(data=data)
print(result.status_code)
print(result.json())