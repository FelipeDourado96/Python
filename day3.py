print("Welcome to Treasure Island\nYour mission is to find the treasure.\nYou're at a cross road. Where do you want to go?\n\tType 'left' or 'right'.")

# Get user input and convert to lowercase for easy comparison
answer = input().lower()

if answer == "left":
    # Player chose left, next scenario
    print("You've come to a lake. There is an island in the middle of the lake.\n\tType 'wait' to wait for a boat ou 'swim' to swim across.")
    answer = input().lower()

    if answer == "wait":
        # Player waits and safely reaches island
        print("You arrive at the island unharmed. There is a house with 3 doors.\n\tOne red, one yellow and one blue. Which color do you choose?")
        answer = input().lower()

        if answer == "yellow":
            # Player chose correct door - wins game
            print("You found the treasure! You won!")
        elif answer == "red":
            # Player chose fire door - game over
            print("It's a room full of fire. Game over.")
        else:
            # Any other door leads to beasts - game over
            print("You entered a room of beasts. Game over.")
    else:
        # Player swims and is attacked - game over
        print("You got attacked by an angry trout. Game over.")
else:
    # Player chose right at the start - game over
    print("You fell into a hole. Game over.")
