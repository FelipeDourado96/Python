from random import randint

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

player = int(input("What do you choose?\n\tType 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
machine = randint(0,2)

if player == 0:
    print(rock)
    if machine == 0:
        print(f"{rock}\nIt's a draw!")
    elif machine == 1:
        print(f"{paper}\nYou lost...")
    else:
        print(f"{scissors}\nYou won!")
elif player == 1:
    print(paper)
    if machine == 0:
        print(f"{rock}\nYou won!")
    elif machine == 1:
        print(f"{paper}\nIt's a draw!")
    else:
        print(f"{scissors}\nYou lost...")
elif player == 2:
    print(scissors)
    if machine == 0:
        print(f"{rock}\nYou lost...")
    elif machine == 1:
        print(f"{paper}\nYou won!")
    else:
        print(f"{scissors}\nIt's a draw!")
else:
    print("Invalid number")