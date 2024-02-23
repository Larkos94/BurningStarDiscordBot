__package__ = "helpers"

import time
import datetime

def get_timestamp(day, hour, min, month = datetime.date.today().month, year = datetime.date.today().year ):
    discord_timestamp = datetime.datetime(year, month, day, hour, min)
    discord_timestamp = '<t:' + str(int(time.mktime(discord_timestamp.timetuple()))) + ':F>'

    return discord_timestamp