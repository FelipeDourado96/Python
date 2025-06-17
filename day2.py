print("Welcome to the tip calculator!")

# Ask user for total bill amount and convert input to float
total = float(input("What was the total bill?\n$"))

# Ask user how much tip percentage they want to give (10, 12, or 15)
tip = int(input("How much tip would you like to give: 10, 12 or 15?\n"))

# Ask user how many people to split the bill between
people = int(input("How many people to split the bill?\n"))

# Check if the tip entered is one of the allowed values
if tip == 10 or tip == 12 or tip == 15:
    # Calculate total bill including tip
    total = total + (total * tip) / 100

    # Calculate the amount each person has to pay, rounded to 2 decimal places
    bill = round(total / people, 2)

    # Print the amount each person should pay
    print(f"Each person should pay: ${bill}")
else:
    # If tip value is not allowed, print error message
    print("Tip value not available")
