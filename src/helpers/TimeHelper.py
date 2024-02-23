__package__ = "helpers"

import time
import datetime
import calendar

def get_timestamp(day, hour, min, month = datetime.date.today().month, year = datetime.date.today().year ):
    discord_timestamp = datetime.datetime(year, month, day, hour, min)
    discord_timestamp = '<t:' + str(int(time.mktime(discord_timestamp.timetuple()))) + ':F>'

    return discord_timestamp

def get_day_name(day, hour, min, month = datetime.date.today().month, year = datetime.date.today().year ):
    discord_timestamp = datetime.datetime(year, month, day, hour, min)
    return calendar.day_name[discord_timestamp.weekday()]
