"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@created: 04-Apr-17
"""
from datetime import datetime

from pytz import timezone, utc


def get_time():
    utc_time = datetime.utcnow()
    utc_time = utc_time.replace(tzinfo=utc)
    local_tz = timezone("Asia/Calcutta")
    local_time = utc_time.astimezone(local_tz)
    local_time = local_time.replace(tzinfo=None)
    return local_time.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == '__main__':
    print(get_time())
