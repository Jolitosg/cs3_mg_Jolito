class Pizza:
    def __init__(self, mushrooms, extra_cheese, peperoni):
        self.mushrooms = mushrooms
        self.extra_cheese = extra_cheese
        self.peperoni = peperoni

    def calculate_total(self):
        self.price = 10 + (self.mushrooms + self.peperoni + self.extra_cheese)*1.5
        return self.price
    def total(self):
        print(self.price, "is the price")
print ("Welcome to the PSHS-WVC Pizza Parlor")

pizza1=Pizza(1, 1, 1)
pizza1.calculate_total()
pizza1.total()