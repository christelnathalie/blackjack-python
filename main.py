import random
import art
from operator import truediv

def deal_cards():
    '''This function gives randomly a card to the user or computer hand) ) '''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(hand):
    '''This function calculates the score of a hand. (according to the ace and blackjack rule) '''
    ## blackjack
    if sum(hand) == 21 and len(hand)==2:
        return 0
    ## ace rules
    if 11 in hand and sum(hand)> 21:
        hand.remove(11)
        hand.append(1)
        return sum(hand)
    return sum(hand)
def compare(u_score, c_score):
    if u_score ==c_score:
        return "🫱🏽‍🫲🏿It is a draw!🫱🏽‍🫲🏿"
    elif c_score==0:
        return "🏴 Computer has a blackjack🏴 "
    elif u_score==0:
        return "🐈‍⬛ You win with a blackjack. 🐈‍⬛"
    elif u_score>21:
        return "😖You went over. You lose.😖"
    elif c_score>21:
        return "🤭 Computer went over. You win!🤭"
    elif u_score>c_score:
        return "👑 You have a higher score, you win! 👑"
    elif c_score>u_score:
        return "😠The computer has a higher score, you lose.😠"
### we first initialised the game and distribute two cards
def play_blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_hand = []
    computer_hand = []
    user_score = -1
    computer_score = -1
    is_game_over = False
    print(art.logo)
    for _ in range(2):
        user_hand.append(random.choice(cards))
        computer_hand.append(random.choice(cards))
    ## first we need
    while not is_game_over:
        user_score = calculate_score(user_hand)
        computer_score= calculate_score(computer_hand)
        print(f"Your hand {user_hand}. Your score: {user_score}")
        print(f"Computer's first card [{computer_hand[0]}].\n")
        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over= True
        else:
            user_should_deal= input("Type 'y' to get another card, type 'n' to pass.").lower()
            if user_should_deal== "y":
                user_hand.append(deal_cards())
            else:
                is_game_over= True
    while computer_score !=0 and computer_score <17:
        computer_hand.append(deal_cards())
        computer_score= calculate_score(computer_hand)
    print(f"The computer hand is {computer_hand} and its final score is: {computer_score}")
    print(compare(user_score,computer_score))
while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n'")== "y":
    play_blackjack()