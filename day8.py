# List of lowercase alphabet letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(original_text, shift_amount):
    # Initialize an empty string to store the encrypted message
    encrypted_text = ''
    # Loop over each letter in the original text
    for letter in original_text:
        # Loop over the alphabet to find the matching letter
        for alph_letter in alphabet:
            # If the letter matches the current alphabet letter
            if alph_letter == letter:
                # Calculate new position with the shift (caesar cipher)
                alph_position = alphabet.index(alph_letter) + shift_amount
                # If position goes beyond 'z', wrap around the alphabet
                if alph_position > 25:
                    alph_position = alph_position - 26
                # Append the encrypted letter to the result
                encrypted_text += alphabet[alph_position]
        # If the character is not a letter (space, punctuation, etc.)
        if letter not in alphabet:
            # Add a space instead (note: this will replace all non-letters with spaces)
            encrypted_text += ' '
    # Print the encrypted message
    print(encrypted_text)

def decode(secret_text, shift_amount):
    # Initialize an empty string to store the decrypted message
    decrypted_text = ''
    # Loop over each letter in the encrypted text
    for letter in secret_text:
        # Loop over the alphabet to find the matching letter
        for alph_letter in alphabet:
            if alph_letter == letter:
                # Calculate original position by subtracting the shift
                alph_position = alphabet.index(alph_letter) - shift_amount
                # If position goes before 'a', wrap around to the end
                if alph_position < 0:
                    alph_position = 26 + alph_position
                # Append the decrypted letter to the result
                decrypted_text += alphabet[alph_position]
        # If the character is not a letter
        if letter not in alphabet:
            # Add a space instead (same note as above)
            decrypted_text += ' '
    # Print the decrypted message
    print(decrypted_text)

def player_decision():
    # Variable to control the main game loop
    keep_game = True
    while keep_game:
        # Ask user if they want to encode or decode
        decision = input("Type 'encode' to encrypt or 'decode' decrypt:\n\t").lower()
        if decision == "encode":
            # Get the message to encode and convert to lowercase
            original_text = input("Type your message:\n\t").lower()
            # Get the shift number from the user
            shift_amount = int(input("Type the shift numer between 1 and 25:\n\t"))
            # Call encode function with inputs
            encode(original_text, shift_amount)
        elif decision == "decode":
            # Get the encrypted message to decode and convert to lowercase
            secret_text = input("Type the encrypted message:\n\t").lower()
            # Get the shift number from the user
            shift_amount = int(input("Type the shift number between 1 and 25:\n\t"))
            # Call decode function with inputs
            decode(secret_text, shift_amount)
        else:
            # Handle invalid input
            print("Invalid option. Please type 'encode' or 'decode'.")
            # Restart the loop without asking to play again
            continue

        # Loop to ask if user wants to play again
        invalid_option = True
        while invalid_option:
            continue_ = input("Type 'yes' if you want to go again. Otherwise type 'no':\n\t")
            if continue_ == "no":
                # Exit the main game loop
                keep_game = False
                invalid_option = False
                print("Goodbye!")
            elif continue_ == "yes":
                # Continue playing, exit this prompt loop
                print("Let's do it again.\n")
                invalid_option = False
            else:
                # Invalid input, ask again
                print("\nNot a valid option. Let's try again.")

# Run the program by calling the main function
player_decision()
