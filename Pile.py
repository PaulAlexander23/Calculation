from Card import Card
import random

class Pile(object):
    def __init__(self, cards):
        self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def display(self):
        for card in self.cards:
            card.display()

    def show(self):
        for card in self.cards:
            card.show()

    def show_top(self):
        self.hide()
        self.cards[-1].show()

    def hide(self):
        for card in self.cards:
            card.hide()

    def append(self, card):
        self.cards.append(card)

    def remove(self, card):
        try:
            self.cards.remove(card)
        except ValueError:
            print "Card not found."

    def search_number(self, number):
        for card in self.cards:
            if card.number == number:
                return card


class Tableau(Pile):    
    def __init__(self, multiplier, cards):
        self.multiplier = multiplier
        super(Tableau,self).__init__(cards)

    def is_valid(self, card):
        if (self.cards[-1].number + self.multiplier - card.number) % 13 == 0:
            return True
        else:
            return False

def main():
    suits = ["clubs","spades","hearts","diamonds"]
    deck = Pile([])
    for suit in suits:
        for n in range(13):
            deck.append(Card(n+1, 5 * int(n/10), suit, True))

    deck.shuffle()

    hand = Pile([deck.cards[i] for i in [3,24,31,45]])

    hand.display()
    print

    card_3 = hand.search_number(3)

    if card_3 is not None:
        card_3.display()

if __name__ == "__main__":
    main()
