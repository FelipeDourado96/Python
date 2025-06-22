from random import choice

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(hand):
    score = sum(hand)
    while score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score

def win_condition(user_score, comp_score):
    if user_score > 21:
        return "You went over. You lose."
    if comp_score > 21:
        return "Opponent went over. You win!"
    if user_score == comp_score:
        return "Draw."
    return "You win!" if user_score > comp_score else "You lose."

def play_blackjack():
    if input("Play Blackjack? Type 'y' to start, 'n' to quit:\t").lower() != 'y':
        return

    user_hand = [choice(cards), choice(cards)]
    comp_hand = [choice(cards), choice(cards)]

    user_score = calculate_score(user_hand)
    comp_score = calculate_score(comp_hand)

    while True:
        print(f"Your cards: {user_hand}, score: {user_score}")
        print(f"Computer's first card: {comp_hand[0]}")

        if user_score > 21:
            break

        if input("Type 'y' to get another card, 'n' to pass:\t").lower() != 'y':
            break

        user_hand.append(choice(cards))
        user_score = calculate_score(user_hand)

    while comp_score < 17:
        comp_hand.append(choice(cards))
        comp_score = calculate_score(comp_hand)

    print(f"\nFinal hands:\nYou: {user_hand}, score: {user_score}\nComputer: {comp_hand}, score: {comp_score}")
    print(win_condition(user_score, comp_score))

play_blackjack()
