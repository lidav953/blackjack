from game import *

def play_blackjack():
    print('Let\'s play Blackjack!')
    deck = Deck()
    player = initialize_player()

    playing = True
    while playing:

        bet = player.bet()
        deck.shuffle()
        player_hand = Hand()
        dealer_hand = Hand()

        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        print('\nYour hand is:')
        print(player_hand.__str__())

        if player_hand.value() == 21: #player blackjack
            print('You have a blackjack.')
            print('The dealer\'s hand is:')
            print(dealer_hand.__str__())
            if dealer_hand.value() == 21:
                print('The dealer also has blackjack, so you pushed.')
            else:
                print('The dealer doesn\'t have blackjack, so you win.')
                player.win(bet, True)
            playing = keep_playing(player)
            break
        
        print('One card in the dealer\'s hand is:')
        dealer_hand.print_dealer_card()

        
        player_stop = False
        while not player_stop:
            while True:
                action = input('Hit(h) or Stand(s)?')
                if action.lower() == 'h':
                    player_hand.add_card(deck.deal())
                    print('Your current hand is')
                    print(player_hand.__str__())
                    print('Current hand value is ' + player_hand.value())
                    break
                elif action.lower() == 's':
                    player_stop = True
                    break
                else:
                    print('Please enter \'h\' or \'s\'')

            if player_hand.value() == 21:
                print('Your hand value is 21, so you automatically stand.')
                player_stop = True
            elif player_hand.value() > 21:
                player_stop = True
        
        if player_hand.value() > 21: #player bust
            player.lose(bet)
            playing = keep_playing(player)
            break

        print('The dealer\'s hand is:')
        print(dealer_hand.__str__())

        while dealer_hand.value() < 17:
            dealer_hand.add_card(deck.deal())
            print('The dealer\'s current hand is:')
            print(dealer_hand.__str__())
        
        if dealer_hand.value() > 21: #dealer bust
        
        elif dealer_hand.value() > player_hand.value(): #dealer wins
        
        elif dealer_hand.value() < player_hand.value(): #player wins
        
        else: #push
                


if __name__ == "__main__":
   play_blackjack()