class Checkout(object):
    class Discount:
        def __init__(self, numItems, price):
            self.numItems = numItems
            self.price = price

    def __init__(self):
        self.prices = {}
        self.dicounts = {}
        self.items = {}

    def addDiscount(self, item, numOfItems, price):
        discount = self.Discount(numOfItems, price)
        self.dicounts[item] = discount

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item not in self.items:
            self.items[item] = 0
        self.items[item] += 1

    def calculateTotal(self):
        total = 0
        for item, cnt in self.items.items():
            discount_total, cnt = self.calculateDiscount(item,cnt)
            total += self.prices[item] * cnt + discount_total
        return total

    def calculateDiscount(self, item, cnt):
        if item not in self.dicounts:
            return 0, cnt
        discount = self.dicounts[item]
        if cnt < discount.numItems:
            return 0, cnt

        numDiscounts = cnt / discount.numItems
        reminder = cnt % discount.numItems
        return numDiscounts * discount.price, reminder
