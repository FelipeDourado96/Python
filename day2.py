print("Welcome to the tip calculator!")
total = float(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give: 10, 12 or 15?\n"))
people = int(input("How many people to split the bill?\n"))
if tip == 10 or tip == 12 or tip == 15:
    total = total + (total*tip)/100
    bill = round(total/people, 2)
    print(f"Each person should pay: ${bill}")
else:
    print("Tip value not available")