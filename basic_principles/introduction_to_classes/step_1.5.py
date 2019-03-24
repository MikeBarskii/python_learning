# https://stepik.org/lesson/24461/step/8?unit=6767
class MoneyBox:

    def __init__(self, capacity):
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v):
        if (self.coins + v) <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v):
            self.coins += v


box = MoneyBox(5)  # moneybox with capacity 5
box.add(2)  # adding 2 coins to moneybox
box.add(3)
print(box.coins)  # moneybox contains 5 coins
box.add(3)  # we can't add more coins
print(box.coins)  # output:5
