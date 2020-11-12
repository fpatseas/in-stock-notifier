import config

from mailjet_rest import Client
from datetime import date, datetime

def send_email(sender, recipients, subject, body):
    try:
        api_key = config.SMTP_API_KEY
        api_secret = config.SMTP_API_SECRET
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')
        data = {
            'Messages':
            [
                {
	                "From": sender,
	                "To": recipients,
	                "Subject": subject,
	                "HTMLPart": body,
	                "CustomID": "AppGettingStartedTest"
                }
            ]
        }
        mailjet.send.create(data=data)
    except Exception as e:
        print(e)

def json_serial(obj):
	if isinstance(obj, (datetime, date)):
		return obj.isoformat()