from group import Group

import datetime
class Sheet(Group):
    def __init__(self, type, price, date):
        self.type = type
        self.price = price
        self.date = date
    
    def add_extra_price(self):
        today = datetime.date.today()
        day = today.day
        daySpan = day - self.date
        if daySpan < 7:
            return int(self.price * 1.1)