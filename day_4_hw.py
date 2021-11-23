
# def shopping_cart():
#     cart = {}
#     while True:
#         question = input(
#             "Would you like to [S]how cart, [A]dd item [D]elete or [Q]uit? ")
#         if question.lower() == 's':
#             print(cart)
#         if question.lower() == 'a':
#             item = input(
#                 "Please enter the item you would like to add to shopping cart: ")
#             quantity = input("How many would you like? ")
#             cart[item] = quantity
#         if question.lower() == 'd':
#             cart.pop(item)
#         if question.lower() == 'q':
#             print("Here's your final order, thanks for shopping with us")
#             print('====================================================')
#             print(cart)
#             break


# shopping_cart()

# HW 4
# Create a class called cart that retains items and has methods to add, remove, and show

cart = {}


class Cart():
    def __init__(self):
        self.retain_items = retain_items

    def Show_Items(self):
   while True:
#         question = input(
#             "Would you like to [S]how cart, [A]dd item [D]elete or [Q]uit? ")
#         if question.lower() == 's':
#             print(cart)

    def Add_Items(self):
        if question.lower() == 'a':
            item = input(
                "Please enter the item you would like to add to shopping cart: ")
            quantity = input("How many would you like? ")
            cart[item] = quantity

    def Remove_Items(self):
