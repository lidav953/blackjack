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
        return 'You currently have ' + str(self.chips) + ' chips.'

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
    print(player.__str__())
    playing = input('Do you want to keep playing? Say \'y\' or \'yes\' for yes, and anything else for no')
    if playing.lower() == 'y' or playing.lower() == 'yes':
        return True
    return False 
        

"""
def player_blackjack(player, bet):
    #Player hand value is 21 in first two cards, so s/he wins 1.5x the bet
    print("You got blackjack.")
    player.win(bet, true)

def player_bust(player, bet):
    #Player busts, so s/he loses
    print("You busted.")
    player.lose(bet)

def player_win(player, bet):
    #Player's hand value is greater than dealer's, so player wins
    print("You won.")
    player.win(bet)

def dealer_bust(player, bet):
    #Dealer busts, so player wins
    print("Dealer busted.")
    player.win(bet)

def dealer_win(player, bet):
    #Dealer's hand value is greater than player's, so player loses
    print("You lost.")
    player.lose(bet)
    
def push(player):
    #Dealer and player have same hand value, so tie
    print("Push")
"""