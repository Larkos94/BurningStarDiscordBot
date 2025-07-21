__package__ = "models"

import jsonpickle
from models.EventModel import EventModel
from helpers.FileHelper import check_file, id_generator

class FloatEventModel(EventModel):
    def __init__(self, day, hour, minute, month, year, data, discription = ""):
        super().__init__(day, hour, minute, month, year, "Float Event", data, discription)

        self.path = './src/files/floatsignup/'
        self.filename = id_generator()
        while check_file(self.path, self.filename):
            self.filename = id_generator()

        if data is None:
            self.dancer_floater = []
            self.security = []
            self.mc = []
            self.dj = []
            self.photographer = []
            self.backup_dancer = []
            self.backup_staff = []
        else:
            self.dancer_floater = data['dancer_floater']
            self.security = data['security']
            self.mc = data['mc']
            self.dj = data['dj']
            self.photographer = data['photographer']
            self.backup_dancer = data['backup_dancer']
            self.backup_staff = data['backup_staff']

    def get_filename(self):
        return self.filename

    def get_signups(self):
        return [self.dancer_floater, 
                self.security, 
                self.mc, 
                self.dj, 
                self.photographer,
                self.backup_dancer, 
                self.backup_staff
                ]

    def signup_floater(self, user):
        if user.name in self.dancer_floater:
            self.dancer_floater.remove(user.name)

            return False
        self.dancer_floater.append(user.name)
        return True

    def signup_security(self, user):
        if user.name in self.security:
            self.security.remove(user.name)

            return False
        self.security.append(user.name)
        return True

    def signup_mc(self, user):
        if user.name in self.mc:
            self.mc.remove(user.name)

            return False
        self.mc.append(user.name)
        return True
    
    def signup_dj(self, user):
        if user.name in self.dj:
            self.dj.remove(user.name)

            return False
        self.dj.append(user.name)
        return True
    
    def signup_photographer(self, user):
        if user.name in self.photographer:
            self.photographer.remove(user.name)

            return False
        self.photographer.append(user.name)
        return True
    
    def signup_backup_dancer(self, user):
        if user.name in self.backup_dancer:
            self.backup_dancer.remove(user.name)

            return False
        self.backup_dancer.append(user.name)

    def signup_backup_staff(self, user):
        if user.name in self.backup_staff:
            self.backup_staff.remove(user.name)

            return False
        self.backup_staff.append(user.name)
        return True
    
    def save_in_file(self):

        data = {
            'dancer_floater': self.dancer_floater,
            'security': self.security,
            'mc': self.mc,
            'dj': self.dj,
            'photographer': self.photographer,
            'backup_dancer': self.backup_dancer,
            'backup_staff': self.backup_staff,
            'day': self.day,
            'hour': self.hour,
            'minute': self.minute,
            'month': self.month,
            'year': self.year,
            'discription': self.discription
        }
        encoded = jsonpickle.encode(data)
        with open(self.path + self.filename + '.json', 'w+') as f:
            f.write(encoded)

