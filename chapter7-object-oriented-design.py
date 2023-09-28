from enum import Enum
import numpy as np
import random
from collections import deque


# 7.1 Deck of Cards: Design the data structures for a generic deck of cards. Explain how you would subclass the
# data structures to implement blackjack.
class Deck(Enum):
    ACE = 1
    JACK = 10
    QUEEN = 10
    KING = 10


class BlackJack:

    def __init__(self):
        self.playerHand = []
        self.dealerHand = []
        self.deckValues = [Deck.ACE, 2, 3, 4, 5, 6, 7, 8, 9, 10, Deck.JACK, Deck.QUEEN, Deck.KING]
        self. shuffledDeck = {}
        self.remainingCards = deque(np.arange(13))

    def shuffle(self):
        position = random.sample(range(1, 14), 13)
        for i in np.arange(13):
            self.shuffledDeck[position[i]] = self.deckValues[i]

    def dealCards(self):
        self.playerHand.append(self.shuffledDeck.get(self.remainingCards.pop()))
        self.playerHand.append(self.shuffledDeck.get(self.remainingCards.pop()))
        self.dealerHand.append(self.shuffledDeck.get(self.remainingCards.pop()))
        self.dealerHand.append(self.shuffledDeck.get(self.remainingCards.pop()))


def main():

    game = BlackJack()
    game.shuffle()

    print('Type deal to deal card or pass to keep your current hand. Type q to quit.')
    user_choice = input()

    if user_choice.lower().startswith('q'):
        print("Goodbye!")
    elif user_choice == 'deal':
        game.dealCards()
        print('Player was dealt cards ' + str(game.playerHand[0]) + ' and ' + str(game.playerHand[1]))
        print('Dealer was dealt cards ' + str(game.dealerHand[0]) + ' and ' + str(game.dealerHand[1]))


if __name__ == '__main__':
    main()
