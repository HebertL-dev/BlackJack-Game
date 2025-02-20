import random

# Deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
flag = True
timess = 0
ace_changed = False

def hand_cards():
    # Choose random cards from the deck
    return random.choice(cards)

def see(player_h, comp_hand):
    global timess  # Declare timess as global

    if timess == 0:
        for i in range(2):
            player_h.append(hand_cards())

        for i in range(len(player_h)):
            if player_h[i] == 11:
                print(f"This is your current hand: {player_h}")
                x0 = int(input("Do you want your Ace to be 1 or 11? "))
                if x0 == 1 or x0 == 11:
                    player_h[i] = x0
                    ace_changed = True

        print(f"This is your current hand: {player_h}")

        for i in range(2):
            comp_hand.append(hand_cards())
        print(f"This is the rival's visible card: {comp_hand[0]}")
    else:
        player_h.append(hand_cards())
        comp_hand.append(hand_cards())

        # If player is over 21 but has an Ace (11)
        if sum(player_h) > 21 and 11 in player_h:
            for i in range(len(player_h)):
                if player_h[i] == 11:
                    x0 = input(f"You are over 21! Do you want to change an Ace from 11 to 1? (yes/no) ").lower()
                    if x0 == "yes":
                        player_h[i] = 1
                        ace_changed = True  # Convert Ace from 11 to 1
                        break  # Stop after converting one Ace

        if sum(player_h) > 21:  # 🔴 Player bust check
            print(f"You lose! Your final hand: {player_h} and rival hand: {comp_hand}")
            return False  # Player loses immediately

        if sum(comp_hand) > 21:  # ✅ Rival bust check only if player is still in the game
            print(f"You win! The rival busted with this hand: {comp_hand} and your hand was: {player_h}")
            return True  # Player wins if rival busts

        # Check if the computer got a Blackjack (21 with the first two cards)
        if sum(comp_hand) == 21:
            print(f"You lose! The rival got a Blackjack with this hand: {comp_hand}")
            return False  # Player loses if rival has 21

        if sum(player_h) < 21:
            print(f"This is your current hand: {player_h}")
        if sum(player_h) == 21:
            print(f"You win with this hand: {player_h} and rival hand: {comp_hand}")
            return True  # Player wins with 21
        else:
            print(f"You lose! Your final hand: {player_h} and rival hand: {comp_hand}")
            return False  # Player loses if no one wins

    timess += 1  # Increment timess globally
    return None  # Return None if the game is ongoing

def dealer_turn(comp_hand):
    # Dealer must take cards until their hand is at least 17
    while sum(comp_hand) < 17:
        comp_hand.append(hand_cards())
        print(f"Dealer draws a card. Dealer's hand: {comp_hand}")
    return comp_hand

player_h = []
comp_hand = []

while flag:
    result = see(player_h, comp_hand)  # Check the game status

    if result is not None:  # If True (win) or False (lose), break the loop
        flag = False  # Exit the loop
        break

    if result is None:  # Continue if the game is ongoing
        x = input("Do you want another card?\nYes or No\n").lower()
        if x == "yes":
            continue  # Continue if the player wants another card
        else:
            print(f"Final hands: Your hand: {player_h}, Rival's hand: {comp_hand}")
            flag = False  # End the game if the player says "no"

            # Dealer's turn: Draw cards until their hand is at least 17
            comp_hand = dealer_turn(comp_hand)

            # Final evaluation after the game ends
            if sum(player_h) > 21:
                print(f"You lose! Your final hand: {player_h} and rival hand: {comp_hand}")
            elif sum(comp_hand) > 21:
                print(f"You win! The rival busted with this hand: {comp_hand} and your hand was: {player_h}")
            elif sum(player_h) > sum(comp_hand):
                print(f"You win with this hand: {player_h} and rival hand: {comp_hand}")
            elif sum(player_h) < sum(comp_hand):
                print(f"You lose! Your final hand: {player_h} and rival hand: {comp_hand}")
            else:
                print(f"It's a tie! Your final hand: {player_h} and rival hand: {comp_hand}")