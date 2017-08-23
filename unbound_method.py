
class Pizza(object):

    def mix_ingredients(self, x, y):
        print ("part of class" )
        return x + y
 
    def cook(self):
        return self.mix_ingredients(self.cheese, self.vegetables)

class Domino(Pizza):
    def __init__(self, vegetables=None, cheese=None):
        self.cheese = cheese
        self.vegetables = vegetables

    def mix_ingredients(self, x, y):
        print ("part of child class" )
        print x+y

    def print_ingredients(self):
        self.cook()

noel_pizza = Domino(cheese="Amul", vegetables="Onion+capsicum")
noel_pizza.print_ingredients()
