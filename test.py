# cart = []
# cost = 0
# print("Welcome, what would you like to buy? ")
# op = input("When you're done shopping, type done. To proceed, press any key   ")
# op = str(op)
# items = ["apple - 1.00",
#          "bannana - 1.50"
#          "orange - 1.25",
#          ]

# def buying():
#     while op is not "done":
#         print(items)
#         buy = input("Whatcha wanna buy? ")
#         buy = str(buy)
#         if buy == "apple":
#             print("apple sucessfully added to cart")
#             cart.append("apple")
#             cost += 1
#             op = input("Type done to proceed to check out. If you wish to continue shopping, press any key")
#         elif buy == "bannana":
#             print("bannana sucessfully added to cart")
#             cart.append("bannana")
#             cost += 1.5
#         elif buy == "orange":
#             print("orange sucessfully added to cart")
#             cart.append("orange")
#             cost += 1.5

# buying()

cart = list
cart = []
cost = int(0)
items =[ {
    "name": "Television",
    "cost": "$ 74.00",
    "Company": "Samsung"},
    {
    "name": "Iphone",
    "cost": "$ 40.00",
    "model": "Apple"},
    {
    "name": "Car",
    "cost": "$ 30.00",
    "model": "Stellantis"},
    {
    "name": "Water",
    "cost": "$ 1250.00",
    "Company": "Fernando Altamirano Luxury Brands",
    
    }
]




shop = input("Welcome, what would you like to buy? Type options to view options. Type done to check out.  ")
shop = str(shop)
while shop is not "done":
    if shop == "options":
        print(items)
        shop = input("What do you wanna buy? Type done to check out ")
    elif shop == str("Television"):
        cart.append("Television")
        cost += float("74.00")
        print("Television added to cart")
        shop = input("What do you wanna buy? Type done to check out ")
    elif shop == str("Iphone"):
        cart.append("Iphone")
        cost += float("40.00")
        print("Iphone added to cart")
        shop = input("What do you wanna buy? Type done to check out ")
    elif shop == str("Car"):
        cart.append("Car")
        cost += float("30.00")
        print("Car added to cart")
        shop = input("What do you wanna buy? Type done to check out ")
    elif shop == str("Water"):
        cart.append("Water")
        cost += float("1250.00")
        print("Water added to cart")
        shop = input("What do you wanna buy? Type done to check out ")
    elif shop == str("done"):
        print(cart)
        print(cost)
        break

print("Thanks for your pruchase! Come back next time!!!")