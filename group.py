class Group:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def addTax(self, totalAmount):
        price = int(totalAmount * 1.1)
        return '{:,}'.format(price)
    
    def addDotto(self, price):
        return '{:,}'.format(price)