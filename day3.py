print("Welcome to Treasure Island\nYour mission is to find the treasure.\nYou're at a cross road. Where do you want to go?\n\tType 'left' or 'right'.")
answer = input().lower()
if answer == "left":
    print("You've come to a lake. There is an island in the middle of the lake.\n\tType 'wait' to wait for a boat ou 'swim' to swim across.")
    answer = input().lower()
    if answer == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.\n\tOne red, one yellow and one blue. Which color do you choose?")
        answer = input().lower()
        if answer == "yellow":
            print("You found the treasure! You won!")
        elif answer == "red":
            print("It's a room full of fire. Game over.")
        else:
            print("You entered a room of beats. Game over.")
    else:
        print("You got attacked by an angry trout. Game over.")
else:
    print("You fell into a hole. Game over.")