#!/usr/bin/env python3
import random
import sys
import os
import time

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'

STARTING_BALANCE = 5000


def main():
    os.system('clear')
    print('''Welcome to Blackjack!

    Rules:

        Try to get as close to 21 without going over!

        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.

        (H)it to take another card.
        (S)tand to stop taking cards.

        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.

        In case of a tie, the bet is returned to the player.

        The dealer stops hitting at 17.''')

    money = STARTING_BALANCE

    while True:
        # check player balance
        if money <= 0:
            print('You are out of money!\n')
            sys.exit()

        # enter players bet
        print('\nMoney: $' + str(money))
        bet = getBet(money)

        # deal cards
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]
        os.system('clear')
        print('Bet: ' + str(bet))

        # handle player actions
        # (loop until player stands or busts)
        while True:
            displayHands(playerHand, dealerHand, False)
            print()

            # check if player busts
            if getHandValue(playerHand) > 21:
                break

            # get players action
            move = getMove(playerHand, money - bet)

            # player doubles down and can increase bet
            if move == 'D':
                os.system('clear')
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Bet: ' + str(bet))

            # hitting or doubling down takes another card
            if move in ('H', 'D'):
                os.system('clear')
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank, suit))
                playerHand.append(newCard)

                # player bust!!
                if getHandValue(playerHand) > 21:
                    os.system('clear')
                    continue

            # standing or doubling down stops players turn
            if move in ('S', 'D'):
                break

        # handle dealer actions
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                os.system('clear')
                print('Dealer hits..')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                # dealer bust!!
                if getHandValue(dealerHand) > 21:
                    break
                input('\nPress Enter to continue..')
                os.system('clear')

        # show final hands
        displayHands(playerHand, dealerHand, True)

        # determine winner
        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        if dealerValue > 21:
            print('\nDealer busts! You win! ${}!'.format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('\nYou lost!')
            money -= bet
        elif playerValue > dealerValue:
            print('\nYou won! ${}!'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print('\nDraw! You get your money back.')

        input('\nPress Enter to continue..')
        os.system('clear')


# ask player how much they want to bet
def getBet(maxBet):
    while True:
        print('\nHow ,much do you want to bet? (1-{}, or Q to Quit)'.format(maxBet))
        bet = input('> ').upper().strip()

        # player quits
        if bet == 'Q':
            os.system('clear')
            print('\nThanks for playing!')
            time.sleep(1)
            os.system('clear')
            sys.exit()

        # invalid entry
        if not bet.isdecimal():
            print('Please enter a number.')
            continue

        # valid bet
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet


def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    os.system('clear')
    print()
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand[1:] + [BACKSIDE])

    print('\nPLAYER: ', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    value = 0
    numberOfAces = 0

    for card in cards:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)

    value += numberOfAces

    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10

    return value


def displayCards(cards):
    rows = ['', '', '', '']

    for i, card in enumerate(cards):
        rows[0] += ' ___  '
        if card == BACKSIDE:
            # Print a card's back:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            # Print the card's front
            rank, suit = card  # The card is a tuple data structure.
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    for row in rows:
        print(row)


def getMove(playerHand, money):
    while True:
        moves = ['(H)it', '(S)tand']

        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()

        if move in ('H', 'S'):
            return move  # Player has entered a valid move.

        if move == 'D' and '(D)ouble down' in moves:
            return move  # Player has entered a valid move.


if __name__ == '__main__':
    main()
