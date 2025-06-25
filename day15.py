# The Coffee Machine has the following flavors
flavors = [
    {"name": "Expresso", "price": 1.50, "amount_of_water": 80, "amount_of_milk": 0, "amount_of_coffee": 18},
    {"name": "Latte", "price": 2.50, "amount_of_water": 200, "amount_of_milk": 150, "amount_of_coffee": 24},
    {"name": "Cappuccino", "price": 3, "amount_of_water": 250, "amount_of_milk": 100, "amount_of_coffee": 24},
]

# The coffee machine has a certain amount of resources
machine_resources = {"amount_of_water": 30000, "amount_of_milk": 5000, "amount_of_coffee": 2000}

# Check if the resources are enough to prepare that drink
def check_resources(order_index):
    if machine_resources["amount_of_water"] < flavors[order_index]["amount_of_water"]:
        print("Sorry, there is not enough water.")
        return False
    elif machine_resources["amount_of_milk"] < flavors[order_index]["amount_of_milk"]:
        print("Sorry, there is not enough milk.")
        return False
    elif machine_resources["amount_of_coffee"] < flavors[order_index]["amount_of_coffee"]:
        print("Sorry, there is not enough coffee.")
        return False
    else:
        return True

def coin_insert():
    print("Please insert coins.")
    quarter = int(input("How many quarters? "))
    dime = int(input("How many dimes? "))
    nickel = int(input("How many nickels? "))
    penny = int(input("How many pennies? "))
    # Add all the coins and check if the user has inserted enough money
    total = (quarter * 0.25) + (dime * 0.10) + (nickel * 0.05) + (penny * 0.01)
    return total

# Welcome message
print("Welcome! What would you like to drink today?\nWe have the following:\nExpresso ($1.50), Latte ($2.50) and Cappuccino ($3.00)")

while True:

    # Get the order
    user_beverage = input("What would you like? Type 'expresso', 'latte', 'cappuccino', or 'report' to check the amount of Water, Milk and Coffee in this machine\n").lower()

    # Check if the user wants the report
    if user_beverage == 'report':
        print(f"Water: {machine_resources['amount_of_water']}ml\nMilk: {machine_resources['amount_of_milk']}ml\nCoffee: {machine_resources['amount_of_coffee']}g")

    # Check if the machine has enough resources
    elif user_beverage in ["expresso", "latte", "cappuccino"]:
        order_index = ["expresso", "latte", "cappuccino"].index(user_beverage)
        if not check_resources(order_index):
            continue

        # Take the money
        total_money_inserted = coin_insert()

        # Check if the money is enough
        if total_money_inserted >= flavors[order_index]["price"]:
            machine_resources["amount_of_water"] -= flavors[order_index]["amount_of_water"]
            machine_resources["amount_of_milk"] -= flavors[order_index]["amount_of_milk"]
            machine_resources["amount_of_coffee"] -= flavors[order_index]["amount_of_coffee"]
            change = round(total_money_inserted - flavors[order_index]["price"], 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            print(f"Here is your {flavors[order_index]["name"]} ☕️. Enjoy!")
        else:
            print("Sorry, there is not enough money. Money refunded")
    else:
        print("Sorry, we don't have what you want")
        break