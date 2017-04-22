class Card:
    def __init__(self, number, value, suit, faceup = False):
        self.value = value
        self.number = number
        self.suit = suit
        self.faceup = faceup

    def show(self):
        self.faceup = True

    def hide(self):
        self.faceup = False

    def display(self):
        if self.faceup:
            print "%d %s " % (self.number, self.suit),


def main():
    suits = ["clubs","spades","hearts","diamonds"]
    deck = []

    for suit in suits:
        for n in range(13):
            deck.append(Card(n+1, 5 * int(n/10), suit))

    deck[3].display()

    deck[3].show()

    deck[3].display()


if __name__ == "__main__":
    main()
