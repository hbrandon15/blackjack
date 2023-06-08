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
    
    
    print(f"Dealer's first card is: {dealer_hand[0]}")
    print(f"Your hand is: {player_hand}")

def calculate_score(card_hand):
   if 11 and 10 in card_hand:
      return 0
   else: 
      return sum(card_hand)

# test_hand1 = [10, 11]
# test_hand2 = [4,6]

# print(calculate_score(test_hand1))
# print(calculate_score(test_hand2))
  

# def hit():
#     """Draws another card and totals sum"""
#     player_hand.append(random.choice(cards))
#     player_score = sum(player_hand)
#     if player_score > 21:
#         print(f"BUST! Score is {player_score} which is over 21. Game over")
#         player_score = 0
#     else:
#       print(f"Your hand is: {player_hand}, with a current score of {player_score}")
#       print(f"Dealer's first card is: {dealer_hand[0]}")
#       player_choice()

# def player_choice():
#     """Gives option to the player on drawing another card or standing"""

#     hit_choice = input("Type 'h' to Hit and get another card OR 's' to Stand\n")
#     if(hit_choice == 'h'):
#       print("You decided to hit")
#       hit()
#     elif(hit_choice == 's'):
#       print("You decided to stand")
#       stand(dealer_hand, dealer_score)

    


# def stand(dealer_hand, dealer_score):
#    print(f"Dealer has {dealer_hand}")
#    dealer_hand.append(random.choice(cards))
#    if(dealer_score > 21): 
#       print("Player WINS!")
#    elif(dealer_score == player_score):
#     print("Draw!")
#    elif(dealer_score > player_score):
#     print("Dealer wins!")
#    else:
#     print("Player wins!")


      
   
    
    
# game_start()




# TODO: #3 Create a function for stand. This is when the dealer will reveal the cards and score. They will hit if needed. 

