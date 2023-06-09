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



def calculate_score(card_hand):
   """Calculate the total score of the given hand"""
   if 11 in card_hand and 10 in card_hand and len(card_hand) == 2:
      return 0 
   if sum(card_hand) > 21 and 11 in card_hand:
    card_hand.remove(11)
    card_hand.append(1)
    return sum(card_hand)
   else:
    return sum(card_hand)

def compare(d_score, p_score):
  """Compare scores between the dealer and player"""
  
  if d_score == p_score:
    print("Its a DRAW!")
  elif d_score > p_score or p_score > 21:
    print(f"Dealer score is {d_score}. Player's score of {p_score}! Dealer wins!")
  elif p_score > d_score or d_score > 21: 
    print(f"Player score is {p_score}. Dealer's score of {d_score}! Player wins!")
  
  
  

def deal_card(hand):
   """Appends a new random card into the given hand"""
   
   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
   hand.append(random.choice(cards))
   return hand
  


def game_restart():
  """Prompts the user to see if they want to restart the game"""
  
  restart = input("Would you like to restart the game? Type 'y' for yes or 'n' for no.\n").lower()
  if restart == 'y':
    game_start()
  elif restart == 'n':
    print("Thank you for playing!")
    
    
  else: 
    print("Please select a valid response")
    game_restart()

def game_start():
  os.system('cls' if os.name == 'nt' else 'clear')
  print(art.logo)
  dealer_hand = []
  player_hand = []
  dealer_score = 0
  player_score = 0
  user_ready = input("Would you like to play a game of Blackjack? Type 'y' for yes or 'n' for no. \n").lower()
  if(user_ready == 'y'):
    print("Game starting...")
    for _ in range(2):
      deal_card(player_hand)
      deal_card(dealer_hand)
    print(f"Dealer's first card: {dealer_hand[0]}")
    while(True):
      player_score = calculate_score(player_hand)
      dealer_score = calculate_score(dealer_hand)
      if dealer_score == 0:
        print(f"Dealer score is {dealer_score}! Game over! Player wins.")
        break
      elif player_score > 21 or player_score == 0:
        print(f"Player score is {player_score}! Game over!")
        break
      else:
        print(f"Your current hand: {player_hand} with a current score of {player_score}")
        hit_choice = input("Type 'h' to Hit and get another card OR 's' to Stand\n")
        if(hit_choice == 'h'):
          print("You decided to hit")
          deal_card(player_hand)
        elif(hit_choice == 's'):
          break
   
    dealer_score = calculate_score(dealer_hand)
    if dealer_score < 17:
        while dealer_score != 0 and dealer_score < 17:
          deal_card(dealer_hand)
          dealer_score = calculate_score(dealer_hand)
    if dealer_score > 21:
      dealer_score = 0
    compare(dealer_score,player_score)
    game_restart()

    
  elif(user_ready == 'n'):
      print("Maybe next time!")
  else:
      print("Invalid input!")
      game_start()

game_start()
   

