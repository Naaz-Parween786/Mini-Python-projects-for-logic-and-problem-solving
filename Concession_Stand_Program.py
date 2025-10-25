# Concession stand program:-

# dictionary {key:value}

menu = {"Pizza": 45.00,
        "Nachos": 40.00,
        "Popcorn": 50.00,
        "Chips": 20.00,
        "Fries": 45.00,
        "Pretzel": 80.50,
        "Soda": 40.00,
        "Lemonade":30.25}

cart = []
total = 0

print("---------MENU---------")
for key, value in menu.items():
    print(f"{key}: ₹{value:.2f}")
print("------------------------")

while True:
    food = input("Select an item (q to quit): ")
    if food.lower() == "q":
        break
    # Match ignoring case
    matched = None
    for key in menu:
        if key.lower() == food.lower():
            matched = key
            break

    if matched:
        cart.append(matched)
        print(f"{matched} added to cart.")
    else:
        print("This item is not on menu. Try again.")


print()
print("------------YOUR ORDER--------------")

# for food in cart:  # it is not working
for i, food in enumerate(cart, start=1):
    total += menu[food]
    print(f"{i}. {food} - ₹{menu[food]:.2f}")

print("------------------------------------")
print(f"Total is: ₹{total:.2f}")

