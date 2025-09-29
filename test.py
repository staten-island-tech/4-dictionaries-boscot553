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
cost = float(0)
items =[ {
    "name": "Television",
    "cost": "$ 74.00",
    "model": "Samsung S95F"},
    {
    "name": "Iphone",
    "cost": "$ 40.00",
    "model": "Falcon Supernova iPhone 6"},
    {
    "name": "Car",
    "cost": "$ 30.00",
    "model": "Rolls-Royce La Rose Noire Droptail"},
]

shop = input("Welcome, what would you like to buy? Type options to view options. Type done to check out.  ")
shop = str(shop)
if shop == "options":
    print(items)
elif shop == str("Television"):
    cart.append("Television")
    cost += 74.00
elif shop == str("Iphone"):
    cart.append("Iphone")
elif shop == str("Car"):
    cart.append("Car")
elif shop == str("done"):
    print(cart)