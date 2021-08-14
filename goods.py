from group import Group

class Goods(Group):
    def __init__(self, goods, price):
        self.goods = goods
        self.price = price

    def add_goods_price(self):
        return self.price
