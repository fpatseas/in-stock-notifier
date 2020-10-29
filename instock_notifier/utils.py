from datetime import date, datetime

def json_serial(obj):
	if isinstance(obj, (datetime, date)):
		return obj.isoformat()