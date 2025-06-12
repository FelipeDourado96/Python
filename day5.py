import random
from random import shuffle

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")

number_of_letters = int(input("How many letter would you like in your password?\n\t"))
number_of_numbers = int(input("How many numbers would you like?\n\t"))
number_of_symbols = int(input("How many symbols would you like?\n\t"))

password = []
final_password = []

for char in range(0,number_of_letters):
    password.append(random.choice(letters))
for char in range(0,number_of_numbers):
    password.append(random.choice(numbers))
for char in range(0, number_of_symbols):
    password.append(random.choice(symbols))

shuffle(password)
final_password = ''.join(password)

print(f"Your password is: {final_password}")