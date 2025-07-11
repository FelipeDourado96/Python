import pandas as pd
df = pd.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")
dictionary = {row.letter:row.code for (index, row) in df.iterrows()}

user_word = input("Enter a word: ").upper()
code_list = [dictionary[letter] for letter in user_word]
print(code_list)