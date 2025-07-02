# The Coffee Machine has the following flavors
flavors = [
    {"name": "espresso", "price": 1.50, "water": 80, "milk": 0, "coffee": 18},
    {"name": "Latte", "price": 2.50, "water": 200, "milk": 150, "coffee": 24},
    {"name": "Cappuccino", "price": 3, "water": 250, "milk": 100, "coffee": 24},
]

# The coffee machine has a certain amount of resources
machine_resources = {"water": 500, "milk": 200, "coffee": 100}
profit = 0

# Check if the resources are enough to prepare that drink
def check_resources(order_index):
    """Returns True when order can be made, False if ingredients are insufficient"""
    for ingredient in machine_resources:
        if machine_resources[ingredient] < flavors[order_index][ingredient]:
            print(f"Sorry, there is not enough {ingredient}")
            return False
    return True

def coin_insert():
    """Returns the total calculated from coins inserted"""
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
        print(f"Water: {machine_resources['water']}ml\nMilk: {machine_resources['milk']}ml\nCoffee: {machine_resources['coffee']}g\nMoney: ${profit}")

    # Check if the machine has enough resources
    elif user_beverage in ["expresso", "latte", "cappuccino"]:
        order_index = ["expresso", "latte", "cappuccino"].index(user_beverage)
        if not check_resources(order_index):
            continue

        # Take the money
        total_money_inserted = coin_insert()

        # Check if the money is enough
        if total_money_inserted >= flavors[order_index]["price"]:
            for item in machine_resources:
                machine_resources[item] -= flavors[order_index][item]
            change = round(total_money_inserted - flavors[order_index]["price"], 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            profit += round(total_money_inserted - change, 2)
            print(f"Here is your {flavors[order_index]["name"]} ☕️. Enjoy!")
        else:
            print("Sorry, there is not enough money. Money refunded")
    else:
        print("Sorry, we don't have what you want")
        break