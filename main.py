import art
import os
import random
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_hand = []
player_hand = []
dealer_score = 0
player_score = 0

def game_start():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(art.logo)
    user_ready = input("Would you like to play a game of Blackjack? Type 'y' for yes or 'n' for no. \n").lower()
    if(user_ready == 'y'):
        print("Game starting...")
        deal_start()
    elif(user_ready == 'n'):
        print("Maybe next time!")
    else:
        print("Invalid input!")
        game_start()

def deal_start():
    for range in(0,2):
      dealer_hand.append(random.choice(cards))
      player_hand.append(random.choice(cards))
    player_score = sum(player_hand)
    
    print(f"Dealer's first card is: {dealer_hand[0]}")
    print(f"Your hand is: {player_hand}, with a current score of {player_score}")
    
    
game_start()




# TODO: #2 Create a hit function that will select another card and add it to the total score

