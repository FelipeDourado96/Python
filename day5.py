import random
from random import shuffle

# Lists of possible characters for the password
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M',
           'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")

# Ask the user how many letters, numbers, and symbols they want in their password
number_of_letters = int(input("How many letters would you like in your password?\n\t"))
number_of_numbers = int(input("How many numbers would you like?\n\t"))
number_of_symbols = int(input("How many symbols would you like?\n\t"))

password = []  # Temporary list to hold password characters

# Add random letters to the password list
for _ in range(number_of_letters):
    password.append(random.choice(letters))

# Add random numbers to the password list
for _ in range(number_of_numbers):
    password.append(random.choice(numbers))

# Add random symbols to the password list
for _ in range(number_of_symbols):
    password.append(random.choice(symbols))

# Shuffle the list so characters are in random order
shuffle(password)

# Join the list into a single string to form the final password
final_password = ''.join(password)

# Output the generated password to the user
print(f"Your password is: {final_password}")
