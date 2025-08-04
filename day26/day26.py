import pandas as pd

df = pd.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")
dictionary = {row.letter:row.code for (index, row) in df.iterrows()}

keep_trying = True
while keep_trying:
    user_word = input("Enter a word: ").upper()
    try:
        code_list = [dictionary[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        keep_trying = False
        print(code_list )