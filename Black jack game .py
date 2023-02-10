# importing random to get random cards from the deck of cards
import random
# Binary variables to know if the player and dealers are in or out
playerIn = True
DealerIN = True
# The dealers card the the player can not see
second_dealer_card = '**'
# Create deck of cards, Player hand and dealer hand
Deck_of_cards = [ 2,3,4,5,6,7,8,9,10,
2,3,4,5,6,7,8,9,10,
2,3,4,5,6,7,8,9,10,
2,3,4,5,6,7,8,9,10,
'J','Q','K','A',
'J','Q','K','A',
'J','Q','K','A',
'J','Q','K','A']

player_hand = []
dealerHand = []
# deal the cards pick random for the deck of cards we have and remove it from the deck
def deal_cards(turn):
    card = random.choice(Deck_of_cards)
    turn.append(card)
    Deck_of_cards.remove(card)

# total of each hand
# the total for J Q and K is 10
# the total of A depends on if the total is above 11 or below 11
def total(turn):
    total = 0
    face = ['J','Q','K']
    for card in turn:
        if card in range(1,11):
            total += card
        elif card in face:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total

#checking for the winner

def understand_dealer_hand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) >2:
        return dealerHand[0],dealerHand[1]
    elif len(dealerHand)>3:
        return dealerHand[0], dealerHand[1],dealerHand[2]


# the actual game
# in the beginning the dealer and the player getting 2 cards with a for loop using the deal cards function
for i in range(2):
    deal_cards(dealerHand)
    deal_cards(player_hand)

#print(dealerHand)
#print(player_hand)
# I made the dealer hands related on if they have 17 or higher to draw another card
while playerIn or DealerIN:
    print(f'The dealer {understand_dealer_hand()} and {second_dealer_card}')
    print(f'You have {player_hand} with sum of {total(player_hand)}')
    if playerIn:
        stay_or_hit = input('press 1 for staying \npress 2 for hit another one: ')
    if total(dealerHand)> 17:
        DealerIN = False
    else:
        deal_cards(dealerHand)

    if stay_or_hit == '1':
        playerIn = False
    else:
        deal_cards(player_hand)

    if total(player_hand) >= 21:
        break
    elif total(dealerHand) >= 21:
        break

if total(player_hand) == 21:
    print(f'you have {player_hand} with {total(player_hand)} and the dealer has {dealerHand} with {total(dealerHand)}')
    print('You won with 21')

elif total(dealerHand) == 21:
    print(f'you have {player_hand} with {total(player_hand)} and the dealer has {dealerHand} with {total(dealerHand)}')
    print('You lost the dealer has 21')

elif total(player_hand) > 21:
    print(f'you have {player_hand} with {total(player_hand)} and the dealer has {dealerHand} with {total(dealerHand)}')
    print('You lost with a total above 21')

elif total(dealerHand) > 21:
    print(f'you have {player_hand} with {total(player_hand)} and the dealer has {dealerHand} with {total(dealerHand)}')
    print('You won the dealer has over 21')

elif 21 - total(dealerHand) < 21 - total(player_hand):
    print(f'you have {player_hand} with {total(player_hand)} and the dealer has {dealerHand} with {total(dealerHand)}')
    print('You lost the dealer win he has higher number')

elif 21 - total(dealerHand) > 21 - total(player_hand):
    print(f'you have {player_hand} with {total(player_hand)} and the dealer has {dealerHand} with {total(dealerHand)}')
    print('You won the dealer  has lower number')
