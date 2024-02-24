__package__ = "models"

from helpers.TimeHelper import get_timestamp, get_day_name

class EventModel:
    def __init__(self, day, hour, minute,month, year, event_type):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.month = month
        self.year = year
        self.event_type = event_type
        self.event_timestamp = get_timestamp(day, hour, minute, month, year)
        self.event_day = get_day_name(day, hour, minute, month, year)

    def update_event_time(self, day, hour, minute):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.event_timestamp = get_timestamp(day, hour, minute)
        self.event_day = get_day_name(day, hour, minute)

    def get_event_timestamp(self):
        return self.event_timestamp
    
    def get_event_day(self):
        return self.event_day
    
    def get_event_type(self):
        return self.event_type

