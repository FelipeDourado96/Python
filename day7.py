from random import choice

# Introductory messages to the player
print("\tLet's Hang'em all!\n")
print("Welcome to the Pokemon Hangman Game\n")

# List of all available Pokémon names (Gen 1) for the game
gen1_pokemon = [
    "Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard",
    "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree",
    "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot",
    "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok",
    "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran♀", "Nidorina",
    "Nidoqueen", "Nidoran♂", "Nidorino", "Nidoking", "Clefairy", "Clefable",
    "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat",
    "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth",
    "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck",
    "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl",
    "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke",
    "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool",
    "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash",
    "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch’d",
    "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder",
    "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno",
    "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor",
    "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing",
    "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan",
    "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie",
    "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir",
    "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee",
    "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar",
    "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos",
    "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew"
]

# Corresponding list of Pokémon types, aligned by index with gen1_pokemon
gen1_types = [
    ["Grass", "Poison"], ["Grass", "Poison"], ["Grass", "Poison"], ["Fire"], ["Fire"], ["Fire", "Flying"],
    ["Water"], ["Water"], ["Water"], ["Bug"], ["Bug"], ["Bug", "Flying"],["Bug", "Poison"], ["Bug", "Poison"],
    ["Bug", "Poison"], ["Normal", "Flying"], ["Normal", "Flying"], ["Normal", "Flying"], ["Normal"], ["Normal"],
    ["Normal", "Flying"], ["Normal", "Flying"], ["Poison"], ["Poison"], ["Electric"], ["Electric"], ["Ground"],
    ["Ground"], ["Poison"], ["Poison"], ["Poison", "Ground"], ["Poison"], ["Poison"], ["Poison", "Ground"],
    ["Fairy"], ["Fairy"], ["Fire"], ["Fire"], ["Normal", "Fairy"], ["Normal", "Fairy"], ["Poison", "Flying"],
    ["Poison", "Flying"], ["Grass", "Poison"], ["Grass", "Poison"], ["Grass", "Poison"], ["Bug", "Grass"], ["Bug", "Grass"],
    ["Bug", "Poison"], ["Bug", "Poison"], ["Ground"], ["Ground"], ["Normal"], ["Normal"], ["Water"], ["Water"], ["Fighting"],
    ["Fighting"], ["Fire"], ["Fire"], ["Water"], ["Water"], ["Water", "Fighting"], ["Psychic"], ["Psychic"], ["Psychic"],
    ["Fighting"], ["Fighting"], ["Fighting"], ["Grass", "Poison"], ["Grass", "Poison"], ["Grass", "Poison"],
    ["Water", "Poison"], ["Water", "Poison"], ["Rock", "Ground"], ["Rock", "Ground"], ["Rock", "Ground"], ["Fire"],
    ["Fire"], ["Water", "Psychic"], ["Water", "Psychic"], ["Electric", "Steel"], ["Electric", "Steel"], ["Normal", "Flying"],
    ["Normal", "Flying"], ["Normal", "Flying"], ["Water"], ["Water", "Ice"], ["Poison"], ["Poison"], ["Water"], ["Water", "Ice"],
    ["Ghost", "Poison"], ["Ghost", "Poison"], ["Ghost", "Poison"], ["Rock", "Ground"], ["Psychic"], ["Psychic"], ["Water"],
    ["Water"], ["Electric"], ["Electric"], ["Grass", "Psychic"], ["Grass", "Psychic"], ["Ground"], ["Ground"], ["Fighting"], ["Fighting"],
    ["Normal"], ["Poison", "Gas"], ["Poison", "Gas"], ["Ground", "Rock"], ["Ground", "Rock"], ["Normal"], ["Grass"],
    ["Normal"], ["Water"], ["Water"], ["Water"], ["Water"], ["Water"], ["Water", "Psychic"], ["Psychic", "Fairy"],
    ["Bug", "Flying"], ["Ice", "Psychic"], ["Electric"], ["Fire"], ["Bug"], ["Normal"], ["Water"], ["Water", "Flying"],
    ["Water", "Ice"], ["Normal"], ["Normal"], ["Water"], ["Water"], ["Electric"], ["Electric"], ["Rock", "Water"], ["Rock", "Water"],
    ["Rock", "Water"], ["Rock", "Water"], ["Rock", "Flying"], ["Normal"], ["Ice", "Flying"], ["Electric", "Flying"], ["Fire", "Flying"],
    ["Dragon"], ["Dragon"], ["Dragon", "Flying"], ["Psychic"], ["Psychic"]
]

# List to keep track of letters the player has guessed so far
guessed_letters = []

# Placeholder string representing the current known letters of the word (starts with all '_')
placeholder = ''

# Randomly select a Pokémon name for the player to guess
word1 = choice(gen1_pokemon)
# Convert the word to lowercase to simplify comparisons
word = word1.lower()

# Initialize the placeholder with underscores, one per letter in the chosen word
for letter in word:
    placeholder += '_'

# Show the initial placeholder to the player (all underscores)
print(placeholder)

# Show a hint by displaying the types of the selected Pokémon
print(f"This pokémon types is/are: {gen1_types[gen1_pokemon.index(word1)]}")

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
