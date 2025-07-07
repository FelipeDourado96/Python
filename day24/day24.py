names_path = "input/names_folder/names.txt"
starting_letter_path = "input/letter_folder/starting_letter.txt"

with open(names_path, "r") as names:
    names = names.readlines()

with open(starting_letter_path, "r") as starting_letter:
    letter_contents = starting_letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace("[name]", stripped_name)
        with open(f"output/letter_for_{stripped_name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)