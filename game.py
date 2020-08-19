import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
values = {'Ace':11, 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10}

class Card:
    #Each card has a suit and a rank.
   
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    #A deck has one card of every suit & rank, for a total of 52 cards
    
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
   
    def __str__(self):
        complete_deck = ''
        for card in self.deck:
            complete_deck += card.__str__() + '\n'
        return 'Current cards in deck are:\n' + complete_deck
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        return self.deck.pop()

class Hand:
    #A hand contains the cards that were dealt to it

    def __init__(self):
        self.hand = []
    
    def __str__(self):
        complete_hand = ''
        for card in self.hand:
            complete_hand += card.__str__() + '\n'
        return complete_hand
    
    def add_card(self, card):
        #Adds a new card to the hand
        self.hand.append(card)
    
    def value(self):
        #Calculate the current value of the cards in hand
        value = 0
        for card in self.hand:
            value += values[card.rank]
            if value>21 and card.rank == 'Ace':
                value -= 10
        return value
    
    def print_dealer_card(self):
        #Shows the dealer's first card
        print(self.hand[0])

class Player:
    #The betting chips that a player has

    def __init__(self, starting_chips):
        self.chips = starting_chips
    
    def __str__(self):
        return 'You now have ' + str(self.chips) + ' chips.'

    def bet(self):
        while True:
            try:
                bet = int(input('How many chips do you want to bet? '))
            except ValueError:
                print('Please enter an integer.')
            else:
                if bet > self.chips:
                    print('You only have ' + str(self.chips) + ' chips to bet.')
                else:
                    return bet

    def win(self, bet, blackjack = False):
        if(blackjack):
            self.chips += bet/2
        self.chips += bet
    
    def lose(self, bet):
        self.chips -= bet

    def get_chips(self):
        return self.chips

def initialize_player():
    #Sets up a player with the number of starting chips that they want.
    while True:
        try:
            starting_chips = int(input('How many chips are you starting with? '))
        except ValueError:
            print('Please enter an integer.')
        else:
            return Player(starting_chips)

def keep_playing(player):
    #Asks the player if they want to keep playing.
    if player.get_chips() == 0:
        print('You have no chips left.')
    else:
        print(player.__str__())
        playing = input('\nDo you want to keep playing? Say \'y\' or \'yes\' for yes, and anything else for no: ')
        if playing.lower() == 'y' or playing.lower() == 'yes':
            return True
    return False 

def player_turn(hand, deck):
        #Goes through the player's turn
        while True: #continue player's turn until the player stands or hand value >= 21
            while True: #get player's action
                action = input('\nHit(h) or Stand(s)? ')
                if action.lower() == 'h':
                    hand.add_card(deck.deal())
                    print('Your current hand is:')
                    print(hand.__str__())
                    print('Current hand value is ' + str(hand.value()) + '.')
                    break
                elif action.lower() == 's':
                    return
                else:
                    print('Please enter \'h\' or \'s\'')

            if hand.value() == 21:
                print('Your hand value is 21, so you automatically stand.')
                return
            elif hand.value() > 21:
                return
    
def dealer_turn(hand, deck):
    #Goes through the dealer's turn
    while hand.value() < 17:
        print('The dealer\'s current hand value is ' + str(hand.value()) + '.')
        print('Dealer gets another card.')
        input('\nPress any key to continue.')
        hand.add_card(deck.deal())
        print('\nThe dealer\'s current hand is:')
        print(hand.__str__())
    return