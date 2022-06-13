from random import shuffle
class Deck:
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}

    def __init__(self, ranks = ranks, suits = suits):
        self.deck = []

        for suit in Deck.suits:
            for rank in Deck.ranks:
                self.deck.append(Card(rank, suit))
        
        #self.shuffle()

    def deal(self):
        try:
            return self.deck.pop()
        except:
            return "Não há mais cartas."
        
    def shuffle(self):
        shuffle(self.deck)

    def showAll(self):
        return self.deck
        
    def __repr__(self):
        return f"A deck containing {len(self.deck)} Cards"



class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __repr__(self):
        return f"Card({self.rank}, {self.suit})"
    
    def __eq__(self, o):
        return self.rank == o.rank and self.suit == o.suit
    
deck01 = Deck()
deck01

deck01.deal()
deck01.showAll()

deck01.shuffle()
deck01.showAll()

deck02 = Deck()
deck02.showAll()

# PP8.5
deck03 = Deck([1,2,3,4,5])
deck03.showAll()

# PP 8.6
card1 = Card("♦", 3)
card1
card2 = Card("♦", 3)
card2
card3 = Card("♠", 5)
card1 == card2
card1 == card3

class Problem:
    def value(self, v):
        self.value = v