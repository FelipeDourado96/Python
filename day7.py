from random import choice

print("\tLet's Hang'em all!\n")
print("Welcome to the Pokemon Hangman Game\n")

    # All words available in the game
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

    # Bank of guessed letters
guessed_letters = []
placeholder = ''

    # Choosing the word and displaying the amount of character
word1 = choice(gen1_pokemon)
word = word1.lower()
for letter in word:
    placeholder += '_'
print(placeholder)

    # Tip
print(f"This pokémon types is/are: {gen1_types[gen1_pokemon.index(word1)]}")

    # Amount of lives
life = 6

    # Win condition is to guess the word correctly
win_condition = False

    # Game loop
while life > 0 and not win_condition:
    guess = input(f"Guessed letters: {guessed_letters}\n\tGuess the letter: ").lower()
    display = ''
    if guess not in guessed_letters and len(guess) == 1:
        guessed_letters.append(guess)
        correct_guess = False
        for index, letter in enumerate(word):
            if guess == letter:
                correct_guess = True
                display += guess
            else:
                display += placeholder[index]
        placeholder = display
        if not correct_guess:
            life -= 1
        if display == word:
            win_condition = True
    elif len(guess) > 1:
        print("You can only type 1 character at time")
    else:
        print("Letter already guessed")
    print(f"Word: {placeholder}")
    print(f"Lives left: {life}")
if win_condition:
    print(f"🎉 Congratulations! You guessed the word: {word1}")
else:
    print(f"💀 Game Over. The word was: {word1}")