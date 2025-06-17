from random import randint  # Import randint to generate random integers

# ASCII art representations for each choice
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)______
          ________)
          _________)
         _________)
---.____________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Ask the player for their choice
player = int(input("What do you choose?\n\tType 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
# Randomly generate the machine's choice (0, 1 or 2)
machine = randint(0, 2)

# Check player's choice and compare with machine's choice
if player == 0:  # Player chose Rock
    print(rock)  # Show player's rock
    if machine == 0:
        print(f"{rock}\nIt's a draw!")  # Machine chose Rock - draw
    elif machine == 1:
        print(f"{paper}\nYou lost...")  # Machine chose Paper - player loses
    else:
        print(f"{scissors}\nYou won!")  # Machine chose Scissors - player wins

elif player == 1:  # Player chose Paper
    print(paper)
    if machine == 0:
        print(f"{rock}\nYou won!")  # Machine Rock - player wins
    elif machine == 1:
        print(f"{paper}\nIt's a draw!")  # Machine Paper - draw
    else:
        print(f"{scissors}\nYou lost...")  # Machine Scissors - player loses

elif player == 2:  # Player chose Scissors
    print(scissors)
    if machine == 0:
        print(f"{rock}\nYou lost...")  # Machine Rock - player loses
    elif machine == 1:
        print(f"{paper}\nYou won!")  # Machine Paper - player wins
    else:
        print(f"{scissors}\nIt's a draw!")  # Machine Scissors - draw

else:
    print("Invalid number")  # Player input outside 0-2
