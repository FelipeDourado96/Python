from day14_data import data
from random import sample, choice
import os

# Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Get random celebrities from the dataset
random_celebrity_1, random_celebrity_2 = sample(data, 2)

# Starting score
score = 0
keep_game = True

# Function to check whether it is correct or not
def check_answer(users_choice, random_celebrity_1, random_celebrity_2):
    if users_choice == 'A':
        if random_celebrity_1["follower_count"] > random_celebrity_2["follower_count"]:
            return True
        else:
            return False
    elif users_choice == 'B':
        if random_celebrity_1["follower_count"] > random_celebrity_2["follower_count"]:
            return False
        else:
            return True
    else:
        return False

# Loop to continue game
while keep_game:
    # Display the name, profession and where is this celebrity from
    print(f"Compare A: {random_celebrity_1['name']}, {random_celebrity_1['description']}, from {random_celebrity_1['country']}.")
    print(f"Against B: {random_celebrity_2['name']}, {random_celebrity_2['description']}, from {random_celebrity_2['country']}.")
    # Take the answer from the user
    users_choice = input("Who has more followers on Instagram? Type 'A' or 'B'\t").upper()
    clear()

    # Check if it is correct
    keep_game = check_answer(users_choice, random_celebrity_1, random_celebrity_2)
    if keep_game:
        score += 1
        print(f"You are right! Current score: {score}")
        random_celebrity_1 = random_celebrity_2
        random_celebrity_2 = choice([celeb for celeb in data if celeb != random_celebrity_1])
    else:
        print(f"Sorry, that's wrong. Final score: {score}")