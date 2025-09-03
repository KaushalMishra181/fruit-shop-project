menu = {
    'Apple': 80,
    'Banana': 40,
    'Orange': 60,
    'Grapes': 120,
    'Pineapple': 150
} 

print("Welcome to the Fruit Shop !")
print("Available Fruits with Price:")
for fruit, price in menu.items():
    print(f"{fruit} : Rs-{price}")

order = 0

while True:
    item = input("\nEnter the item you want to buy: ")

    if item in menu:
        order += menu[item]
        print(f"{item} added to the cart. Current Total: Rs-{order}")
    else:
        print(f"{item} is not available.")

    more = input("Do you want to buy more items? (Yes/No): ").strip().lower()
    if more != "yes":
        break

print(f"\nYour Total Bill is: Rs-{order}")
print("Thank you for visiting!")
