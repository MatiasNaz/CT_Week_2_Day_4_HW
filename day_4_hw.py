# # # Exercise 1:
class shoppingCart():

    def __init__(self):
        self.cart = {}

    def goShop(self):

        while True:
            question = input("Would you like to [S]how cart, [A]dd item [D]elete or [Q]uit? ")
            
            if question.lower() == 's':
                self.displayItems()
            if question.lower() == 'a':
                item = input("Please enter the item you would like to add to shopping cart: ")
                quantity = input(f"How many {item} would you like? ")
                self.cart[item] = quantity
            if question.lower() == 'd':
                del self.cart[item][quantity]
            if question.lower() == 'q':
                self.quitTransaction()
                break

    def displayItems(self):
        print(self.cart)

    def quitTransaction(self):
        while True:
            print("Here's your final order, thanks for shopping with us")
            print('====================================================')
            print(self.cart)
        
            break


my_cart = shoppingCart()
my_cart.goShop()


# Exercise 2:

class myClass():
    def __init__(self):
        self.name = " "

    def get_String(self):
        self.name = input('type in words here: ')

    def print_String(self):
        print(f'{self.name.upper()}')


access = myClass()
access.get_String()
access.print_String()

