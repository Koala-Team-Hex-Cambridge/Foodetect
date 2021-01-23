# This is a sample Python script.

class Food:

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def get_name(self):
        return self.name

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity


class Fridge:

    number_of_food = 0

    def __init__(self, name1):
        self.name1 = name1
        Fridge.number_of_food += 1
        self.foods = []

    def add_food(self, food):
        if Food.quantity > 0:
            self.foods.append(Food)
            Fridge.number_of_food += 1
            return True
        return False


num = 1

with open('test.txt', 'r') as f:
    content = f.readline(num)

while len(content) > 0:
    food1 = Food("content", 1)
    num += 1





