#ch16 Week 12 Homework for James Porter CIS3145
import random

rank = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suit = ["Clubs", "Diamonds", "Hearts", "Spades"]


class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value
    
    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)
    
class Deck:
    def __init__(self):
        self.deck = []
        self.deck = [Card(i,j,rank.index(j)+1) for i in suit for j in rank]

    def shuffle(self):
        random.shuffle(self.deck)

    def dealCard(self):
        return self.deck.pop()

    def count(self):
        return len(self.deck)

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >= 52:
            raise StopIteration
        self.__index += 1
        return self.deck[self.__index-1]
    

class Hand:
    def __init__(self):
        self.cards=[]

    def addCard(self, card):
        self.cards.append(card)

    def playCard(self, index=0):
        return self.cards.pop(index)

    def count(self):
        return len(self.cards)

    def totalPoints(self):
        total_p = [i.value for i in self.cards]
        return sum(total_p)

    def __next__(self):
        if self.index >= self.count():
            raise StopIteration
        self.index += 1
        return self.cards[self.index -1]

    def __iter__(self):
        self.index = 0
        return self
