'''
This is for me to test certain things before trying to implement them into my project
'''

'''
First step, identify how to shuffle cards. I'm thinking that I can try using something from importing random similar to what Dylan did with generating random Pokemon team of 6.
I'm thinking that would be helpful to dish out a "random" card from the deck. Also need to figure out how to shuffle the cards. Random library has a shuffle method and I need to
first understand the syntax and how the shuffle actually works.
'''
import random
from random import shuffle

# This looks like it shuffles the list properly. Can use this for the start of the BlackJack game because it is supposed to start with a deck shuffle.
test_list = ['ace', 'two', 'three', 'four']
shuffle(test_list)
print(test_list)

'''
For the cards itself, I am thinking a dictionary but that might be a really long dictionary and be a lot of keying in. I could have a list under each suit name with the
values spades = [1,2,3,4, etc.] and then have a deck append the suits. I could try labeling the cards like s1,s2,s3 for spades to denote the different suits.
I think maybe tuples could work too but idk much about tuples so but I think they are (x,y) and I think I can set the tuples  as an integer and string. Play around with
tuples and see if they can be appended and indexed into.
'''

test_tup = (1, 'Spades')
# can index into it just like a list which would be (0, 1)
print(test_tup[0])
deck_list = []
card_tups = [(1, 'Spades'), (2, 'Spades'), (3, 'Spades'), (4, 'Spades')]
deck_list.append(card_tups)
# I can append it but it looks like it stick the list within my list
print(deck_list)

# trying to append with a method
card_tups2 = [(1, 'Spades'), (2, 'Spades'), (3, 'Spades'), (4, 'Spades')]
def deck_append(card_suits):
    deck_list2 = []
    for card in card_suits:
        print(card)
        deck_list2.append(card)
    print(deck_list2)
# it appends these, but now I just need to find a way to actually implement these into game format
deck_append(card_tups2)

'''
going to test now to see if there is a way I can get a random card from a deck list
'''

test_deck = [(1, 'Spades'), (2, 'Spades'), (3, 'Spades'), (4, 'Spades')]
print(random.choice(test_deck), 'random card')

'''
another idea i could try is maybe just have a list of the values [1,2,3,4 etc.]
and another list with just the suits [spades, clubs, hearts, diamonds]
and randomly pick from values and then suits to make a card:
pulls 2 from values and spades from suits = 2 of spades.
then I can try storing that somewhere as a tuple so that if that card is generated again,
it can't pick that card again and will just pick another if a tuple is trying to be entered
'''

test_deck_2_suit = ['spades', 'hearts', 'clubs', 'diamonds']
test_deck_2_values = ['A',1,2,3,4,5,6,7,8,9,10,'J','Q','K']

def test_deck_2(card_value, card_suit):
    print('test_deck_2')
    card_given = []
    while True:
        hit = input('Want to take a card? ').lower()
        if hit in ('y', 'yes'):
            card_received = (random.choice(card_value),random.choice(card_suit))
            print(card_received)
            if card_received not in card_given:
                card_given.append(card_received)
            else:
                print('This card was used, getting new card')
                card_received = (random.choice(card_value),random.choice(card_suit))
        else:
            break

test_deck_2(test_deck_2_values,test_deck_2_suit)
# for a very rough draft, this code is similar to what I would want it to do. I think I might go with this method

'''
now I just need to manage to append to my desk_list so I can pull from it. so I want every card possbility in my deck
when card is used, it should be removed from deck.
'''
suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', "K"]
def make_deck(card_suits, card_values):
    deck = []
    for suit in card_suits:
        for value in card_values:
            deck.append((suit, value))
    print(deck)
    print(len(deck))

make_deck(suits,values)


'''
neverm mind, I found out how I would implement the cards. so i will shuffle the deck and just pull the [0] index which
is like pulling a card from the top. the card should already be random because of the shuffle. i can add that card to player
hand and then remove it from the deck so that it cannot be used again.
'''

'''
off play blackjack method: results show it works so far on giving the cards and removing them from deck
The dealer shuffles the deck.
[('A', 'Clubs'), ('J', 'Spades'), (8, 'Diamonds'), (8, 'Hearts'), (4, 'Clubs'), (7, 'Diamonds'), (2, 'Spades'), (7, 'Hearts'), ('K', 'Spades'), (8, 'Spades'), ('A', 'Diamonds'), (10, 'Spades'), (10, 'Hearts'), (7, 'Clubs'), (3, 'Spades'), (8, 'Clubs'), ('K', 'Clubs'), ('A', 'Spades'), ('K', 'Hearts'), (2, 'Diamonds'), (3, 'Diamonds'), (4, 'Hearts'), (5, 'Clubs'), (10, 'Clubs'), (4, 'Spades'), (9, 'Hearts'), (3, 'Clubs'), ('J', 'Clubs'), (10, 'Diamonds'), (5, 'Diamonds'), ('Q', 'Clubs'), (6, 'Diamonds'), ('J', 'Hearts'), ('Q', 'Hearts'), (9, 'Diamonds'), (2, 'Hearts'), (9, 'Clubs'), (4, 'Diamonds'), (5, 'Hearts'), (2, 'Clubs'), (3, 'Hearts'), ('Q', 
'Diamonds'), (7, 'Spades'), ('K', 'Diamonds'), ('A', 'Hearts'), (9, 'Spades'), ('Q', 'Spades'), ('J', 'Diamonds'), (6, 'Hearts'), (5, 'Spades'), (6, 'Clubs'), (6, 'Spades')] after shuffle
The dealer passes out the cards.
[('A', 'Clubs')]
[('J', 'Spades')]
[('A', 'Clubs'), (8, 'Diamonds')]
[('J', 'Spades'), (8, 'Hearts')]

BUT I think I will separate this initial deal into a separate method
'''


'''
Testing how to calculate a hand now. I will use list of 2 tuples to represent cards and see if it's returning it right
'''
test_hand = [('A', 'Spades'), (10, 'Hearts')]

def calc_hand(hand):
    value = 0
    num_aces = 0
    print(hand)
    for card in hand:
        card_value = card[0]
        if card_value in ('K', 'Q', 'J'):
            value += 10
        elif card_value == 'A':
            value += 11
            num_aces += 1
        else:
            value += card_value
    print(value)
    while value > 21 and num_aces > 0:
        value -= 10

    if value > 21:
        print('You lose!')
    elif value == 21:
        print('You win!')
    else:
        print('Take another card?')

calc_hand(test_hand)
