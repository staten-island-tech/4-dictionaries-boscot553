cart = []
cost = 0
print("Welcome, what would you like to buy? ")
op = input("When you're done shopping, type done. To proceed, press any key   ")
op = str(op)
items = ["apple - 1.00",
         "bannana - 1.50"
         "orange - 1.25",
         ]

def buying():
    while op is not "done":
        print(items)
        buy = input("Whatcha wanna buy? ")
        buy = str(buy)
        if buy == "apple":
            print("apple sucessfully added to cart")
            cart.append("apple")
            cost += 1
            op = input("Type done to proceed to check out. If you wish to continue shopping, press any key")
        elif buy == "bannana":
            print("bannana sucessfully added to cart")
            cart.append("bannana")
            cost += 1.5
        elif buy == "orange":
            print("orange sucessfully added to cart")
            cart.append("orange")
            cost += 1.5

buying()

