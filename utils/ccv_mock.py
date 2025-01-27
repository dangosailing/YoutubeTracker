
from random import randrange
from datetime import datetime, timedelta
from time import sleep

def mock_ccv(min_ccv, max_ccv, timestamp):
    """Generate a CCV value and a timestamp"""
    ccv = randrange(min_ccv, max_ccv)
    return {"ccv": ccv, "timestamp": timestamp}

def mock_sample(use_timer=False, timer_interval_seconds=1):
    ccv_data = []
    sec = 0
    while len(ccv_data) < 100:
        timestamp = datetime.now()+timedelta(seconds=sec)
        timestamp_formatted=timestamp.strftime("%H:%M:%S")
        ccv_data.append(mock_ccv(5000, 6000, timestamp_formatted))
        sec+=1
        if use_timer:
            sleep(timer_interval_seconds)
    return ccv_data
