import os  # Import the os module to run system commands

# Function to clear the terminal screen depending on the OS
def clear_screen():
    # Runs 'cls' command on Windows, 'clear' on Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')


def bid():
    persons = []          # List to store dictionaries with each bidder's name and bid
    current_bid = 0       # Variable to keep track of the highest bid so far
    best_bidder = ''      # Variable to store the name of the highest bidder
    keep_bidding = True   # Flag to control the main bidding loop

    while keep_bidding:   # While the auction is still ongoing
        wrong_answer = True

        # Ask for the bidder’s name
        person_name = input("\nWhat's your name?\n\t")

        # Ask for the bid amount and convert it to an integer
        person_bid = int(input("\nWhat's your bid?\n\t$"))

        # Append a dictionary with the bidder’s name and bid to the list
        persons.append({person_name: person_bid})

        # Loop to validate if there are more bidders
        while wrong_answer:
            # Ask if there are other bidders, convert input to lowercase
            continue_bid_game = input(
                "Are there any other bidders? Type 'yes' for yes and 'no' for no\n\t").lower()

            if continue_bid_game == 'no':
                # If no more bidders, end the bidding loop
                keep_bidding = False
                wrong_answer = False

                # Clear the screen before showing results
                clear_screen()

            elif continue_bid_game == 'yes':
                # If there are more bidders, continue the loop
                wrong_answer = False

                # Clear the screen for the next bidder
                clear_screen()

            else:
                # If input is invalid, prompt again
                print("\nSorry, I didn't understand. Let's try again.")

    # After bidding ends, iterate through all bids to find the highest
    for person in persons:
        for name in person:
            # Check if this bid is greater or equal to current highest bid
            if person[name] >= current_bid:
                current_bid = person[name]  # Update highest bid
                best_bidder = name          # Update highest bidder’s name

    # Print the winner and their bid
    print(f"The winner is {best_bidder} with a bid of {current_bid}")


# Run the bidding function to start the program
bid()
