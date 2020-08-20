from datetime import datetime

def get_timestamp():
    time=datetime.now()
    formatted_time=time.strftime("%Y%m%d%H%M%S")
    return formatted_time