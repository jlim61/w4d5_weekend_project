import random
from random import shuffle

class BlackJack():

    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.cards = Cards()
        self.play_option()

 # ----------------Ask Player if Want to Play Method---------------------------       
    
    def play_option(self):
        flag = True
        while flag:
            play_input = input('Would you like to play a game of Black Jack: [y]es/[n]o: ').lower()
            if play_input in ('y', 'yes'):
                self.play_blackjack()
                flag = False
            elif play_input in ('n', 'no'):
                flag = False
            else:
                print('Please enter a valid input.')

# ----------------Playing Black Jack Method---------------------------

    def play_blackjack(self):
        print(f'Welcome to the table {self.player.name}!\nWe are playing with the following deck:\n')
        self.cards.make_deck()
        print('\nThe dealer shuffles the deck.')
        self.cards.shuffle_deck()
        # print(self.cards.deck, 'after shuffle')
        print('The dealer passes out starting cards.')
        self.initial_deal()
        if self.blackjack_check() == 21:
            return
        else:
            self.calculate_hand_value()
            self.hit_option()

## ----------------Deal Initial Hands Method---------------------------

    def initial_deal(self):
        self.player.player_hand.append(self.cards.deck[0])
        self.cards.deck.remove(self.cards.deck[0])
        self.dealer.dealer_hand.append(self.cards.deck[0])
        self.cards.deck.remove(self.cards.deck[0])
        self.player.player_hand.append(self.cards.deck[0])
        self.cards.deck.remove(self.cards.deck[0])
        self.dealer.dealer_hand.append(self.cards.deck[0])
        self.cards.deck.remove(self.cards.deck[0])
        # print(f'Your Hand: {self.player.player_hand}')
        print(f'Dealer Hand: {self.dealer.dealer_hand[0]}, (unknown card)')

# ----------------Check if Player Got Black Jack on First Hand Method---------------------------
    def blackjack_check(self):
        self.player.playervalue = 0
        num_aces = 0
        for card in self.player.player_hand:
            card_value = card[0]
            if card_value in ('K', 'Q', 'J'):
                self.player.playervalue += 10
            elif card_value == 'A':
                self.player.playervalue += 11
                num_aces += 1
            else:
                self.player.playervalue += card_value
        while self.player.playervalue > 21 and num_aces > 0:
            self.player.playervalue -= 10

        if self.player.playervalue == 21:
            print(f'BLACKJACK! You win!\nYour Hand: {self.player.player_hand} Value: {self.player.playervalue}'  )
            return self.player.playervalue

# ----------------Calculate Current Hand Value Method---------------------------

    def calculate_hand_value(self):
        self.player.playervalue = 0
        num_aces = 0
        for card in self.player.player_hand:
            card_value = card[0]
            if card_value in ('K', 'Q', 'J'):
                self.player.playervalue += 10
            elif card_value == 'A':
                self.player.playervalue += 11
                num_aces += 1
            else:
                self.player.playervalue += card_value

        while self.player.playervalue > 21 and num_aces > 0:
            self.player.playervalue -= 10
            num_aces -= 1

        if self.player.playervalue > 21:
            return self.player.playervalue
        else:
            print(f'Your Hand: {self.player.player_hand} Value: {self.player.playervalue}')
        return self.player.playervalue

# ----------------Player's Hit Option Method---------------------------

    def hit_option(self):
        no_bust = True
        player_hand_value = self.calculate_hand_value()
        while no_bust:
            hit_input = input('Would you like to [hit] or [stay]? ').lower()
            if hit_input in ('hit', 'h'):
                player_hand_value = self.receive_card()
                if player_hand_value == 'bust':
                    break
            elif hit_input in ('stay', 's'):
                self.dealer_hand_check()
                print(f'The dealer reveals his hand: {self.dealer.dealer_hand} Value: {self.dealer.dealervalue}')
                if self.dealer.dealervalue < player_hand_value:
                    self.dealer_take_card()
                self.final_check()
                break
            else:
                print('Please enter a valid input.')


# ----------------Player Receives Card Method----------------------
    def receive_card(self):
        self.player.player_hand.append(self.cards.deck[0])
        self.cards.deck.remove(self.cards.deck[0])
        hand_value = self.calculate_hand_value()
        if hand_value > 21:
            print(f'BUST!\nYour Hand: {self.player.player_hand} Value: {hand_value}')
            return 'bust'
        else:
            return hand_value


# ----------------Dealer Takes Card Method----------------------
    def dealer_take_card(self):
        while self.dealer.dealervalue <= 21 and self.dealer.dealervalue < self.player.playervalue:
            print('The dealer takes a card.')
            self.dealer.dealer_hand.append(self.cards.deck[0])
            self.cards.deck.remove(self.cards.deck[0])
            self.dealer_hand_check()
            if self.dealer.dealervalue <= 21:
                print(f'Dealer\'s New Hand: {self.dealer.dealer_hand} Value: {self.dealer.dealervalue}')


# ----------Dealer Hand Check--------------------
    def dealer_hand_check(self):
        self.dealer.dealervalue = 0
        dealer_num_aces = 0
        for card in self.dealer.dealer_hand:
            card_value = card[0]
            if card_value in ('K', 'Q', 'J'):
                self.dealer.dealervalue += 10
            elif card_value == 'A':
                self.dealer.dealervalue += 11
                dealer_num_aces += 1
            else:
                self.dealer.dealervalue += card_value
        while self.dealer.dealervalue > 21 and dealer_num_aces > 0:
            self.dealer.dealervalue -= 10
        if self.dealer.dealervalue > 21:
            print(f'The dealer busts.')
            return self.dealer.dealervalue
        else:
            return self.dealer.dealervalue

# ----------------Final Hand Value vs Dealer Hand Method---------------------------
    def final_check(self):

        if self.player.playervalue < self.dealer.dealervalue and self.dealer.dealervalue <= 21:
            print(f'{self.player.name}\'s Hand: {self.player.player_hand} {self.player.name}\'s Value: {self.player.playervalue}\nDealer Hand:  {self.dealer.dealer_hand} Dealer Value: {self.dealer.dealervalue}')
            print('You lose')
        elif self.player.playervalue <= 21 and self.dealer.dealervalue > 21:
            print(f'{self.player.name}\'s Hand: {self.player.player_hand} {self.player.name}\'s Value: {self.player.playervalue}\nDealer Hand:  {self.dealer.dealer_hand} Dealer Value: {self.dealer.dealervalue}')
            print('You win')
        elif self.player.playervalue <= 21 and self.player.playervalue > self.dealer.dealervalue:
            print(f'{self.player.name}\'s Hand: {self.player.player_hand} {self.player.name}\'s Value: {self.player.playervalue}\nDealer Hand:  {self.dealer.dealer_hand} Dealer Value: {self.dealer.dealervalue}')
            print('You win') 
        elif self.player.playervalue > self.dealer.dealervalue:
            print('The dealer takes another card.')
            self.dealer_take_card()
            self.final_check()
        else:
            print(f'{self.player.name}\'s Hand: {self.player.player_hand} {self.player.name}\'s Value: {self.player.playervalue}\nDealer Hand:  {self.dealer.dealer_hand} Dealer Value: {self.dealer.dealervalue}')
            print("It's a tie.")



# -----------------------------Card Class---------------------------------

class Cards():

    def __init__(self):
        self.suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        self.values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', "K"]
        self.deck = []

# ----------------Making Deck Method---------------------------

    def make_deck(self):
        for suit in self.suits:
            for value in self.values:
                self.deck.append((value, suit))
        print(self.deck)
        print('Number of cards:',len(self.deck))

# ----------------Shuffle Deck Method---------------------------

    def shuffle_deck(self):
        shuffle(self.deck)
        # proof that it's shuffling with print statement
        # print(self.deck)

# -----------------------------Player Class---------------------------------

class Player():

    def __init__(self):
        self.name = None
        self.get_name()
        self.player_hand = []
        self.playervalue = 0

    def __repr__(self):
        return f'Welcome {self.name}!'
    
# ----------------Get Player's Name Method---------------------------

    def get_name(self):
        player_name = input('What is your name? ')
        self.name = player_name
        print(f'Welcome {self.name}!')





# -----------------------------Dealer Class---------------------------------

class Dealer():

    def __init__(self):
        self.dealer_hand = []
        self.dealervalue = 0




'''
tested that making a deck works from sandbox translation into my class
'''
# test_card = Cards()
# test_card.make_deck()
# test_card.shuffle_deck()


'''
getting player name to work
'''
# player = Player()
# print(player)

'''
testing play blackjack method and have blackjack isntantiate with cards and player.
'''
test = BlackJack()
# test.play_blackjack()
