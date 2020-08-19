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
        print('Current hand value is ' + str(player_hand.value()) + '.')

        if player_hand.value() == 21: #player blackjack
            print('You have a blackjack.')
            print('\nThe dealer\'s hand is:')
            print(dealer_hand.__str__())
            if dealer_hand.value() == 21:
                print('\nThe dealer also has blackjack, so you pushed.')
            else:
                print('\nThe dealer doesn\'t have blackjack, so you win.')
                player.win(bet, True)
            playing = keep_playing(player)
            continue
        
        print('\nOne card in the dealer\'s hand is:')
        dealer_hand.print_dealer_card()

        player_turn(player_hand, deck)
        
        if player_hand.value() > 21: #player bust
            print('You busted.')
            player.lose(bet)
            playing = keep_playing(player)
            continue

        print('The dealer\'s hand is:')
        print(dealer_hand.__str__())
        print('The dealer\'s hand value is ' + str(dealer_hand.value()) + '.')

        dealer_turn(dealer_hand, deck)
        
        if dealer_hand.value() > 21: #dealer bust
            print('The dealer busted, so you win.')
            player.win(bet)
        elif dealer_hand.value() == player_hand.value(): #push
            print('Both hands have value ' + str(player_hand.value()))
            print('It\'s a push')
        else:
            print('Your hand\'s value is ' + str(player_hand.value()))
            print('The dealer\'s hand\'s value is ' + str(dealer_hand.value()))
            if dealer_hand.value() > player_hand.value(): #dealer wins
                print('The dealer wins.')
                player.lose(bet)
            else: #player wins
                print('You win.')
                player.win(bet)
        playing = keep_playing(player)

    print('\nThanks for playing!')

if __name__ == "__main__":
   play_blackjack()