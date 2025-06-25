from random import choice
from day7_data import pokemon_names, pokemon_types

# Introductory messages to the player
print("\tLet's Hang'em all!\n")
print("Welcome to the Pokemon Hangman Game\n")





# List to keep track of letters the player has guessed so far
guessed_letters = []

# Placeholder string representing the current known letters of the word (starts with all '_')
placeholder = ''

# Randomly select a Pokémon name for the player to guess
word1 = choice(pokemon_names)
# Convert the word to lowercase to simplify comparisons
word = word1.lower()

# Initialize the placeholder with underscores, one per letter in the chosen word
for letter in word:
    placeholder += '_'

# Show the initial placeholder to the player (all underscores)
print(placeholder)

# Show a hint by displaying the types of the selected Pokémon
print(f"This pokémon types is/are: {pokemon_types[pokemon_names.index(word1)]}")

# Number of allowed wrong guesses before the game ends
life = 6

# Variable to track whether the player has won
win_condition = False

# Main game loop: runs while player still has lives and hasn't won yet
while life > 0 and not win_condition:
    # Ask the player to guess a letter and show already guessed letters
    guess = input(f"Guessed letters: {guessed_letters}\n\tGuess the letter: ").lower()
    display = ''  # Temporary string to build the updated placeholder

    # Check if the guess is a single letter not guessed before
    if guess not in guessed_letters and len(guess) == 1:
        guessed_letters.append(guess)  # Add guess to guessed letters
        correct_guess = False  # Track if the guess was correct this turn

        # Loop through each letter of the word and update the display string
        for index, letter in enumerate(word):
            if guess == letter:
                correct_guess = True
                display += guess  # Reveal the correctly guessed letter
            else:
                display += placeholder[index]  # Keep the previous state (underscore or guessed letter)

        placeholder = display  # Update the placeholder with new guesses

        # If the guess was wrong, subtract a life
        if not correct_guess:
            life -= 1

        # Check if the word is fully guessed
        if display == word:
            win_condition = True

    # If input is more than one character, notify the player
    elif len(guess) > 1:
        print("You can only type 1 character at time")

    # If letter already guessed, notify the player
    else:
        print("Letter already guessed")

    # Show the current state of the word and remaining lives
    print(f"Word: {placeholder}")
    print(f"Lives left: {life}")

# After the loop ends, check if player won or lost and print appropriate message
if win_condition:
    print(f"🎉 Congratulations! You guessed the word: {word1}")
else:
    print(f"💀 Game Over. The word was: {word1}")
