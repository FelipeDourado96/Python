from random import choice

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Good luck!")

def define_difficulty():
    user_difficulty = input("Choose the difficulty: 'easy' or 'hard':\t").lower()
    if user_difficulty == 'easy':
        amount_of_attempts = 10
        print(f"\nYou have {amount_of_attempts} attempts to guess the number.")
        return amount_of_attempts
    elif user_difficulty == 'hard':
        amount_of_attempts = 5
        print(f"\nYou have {amount_of_attempts} attempts to guess the number.")
        return amount_of_attempts
    else:
        amount_of_attempts = 2
        print(f"\nAs you typed wrongly, you will play on Extreme Mode.\nYou have {amount_of_attempts} attempts")
        return amount_of_attempts

def guess(number_guessed, correct_number):
    if number_guessed == correct_number:
        return True
    elif number_guessed > correct_number:
        print("Too high.")
        return False
    else:
        print("Too low.")
        return False

def play_game(amount_of_attempts):
    correct_number = choice(range(1, 101))
    win_condition = False
    while not win_condition and amount_of_attempts > 0:
        try:
            number_guessed = int(input("Make a guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        win_condition = guess(number_guessed, correct_number)
        if win_condition:
            print(f"You got it! The Answer was really {correct_number}.")
        else:
            amount_of_attempts -= 1
            print(f"Guess again.\nYou have {amount_of_attempts} remaining.")
    if not win_condition:
        print(f"End of game. You lost\nThe answer was {correct_number}.")

if __name__ == '__main__':
    user_wants_to_play = True
    while user_wants_to_play:
        amount_of_attempts = define_difficulty()
        play_game(amount_of_attempts)
        keep_playing = input("Do you want to try again? Type 'yes' or 'no': ").lower()
        if keep_playing == 'no':
            break
        elif keep_playing == 'yes':
            print("Ok, good luck!")
        else:
            print("I'm gonna take that as a yes.")
