from Card import Card
from Pile import Pile, Tableau

class Layout:
    def __init__(self, stock, tableau, foundations):
        self.stock = stock
        self.stock.show_top()
        self.tableau = tableau
        for pile in self.tableau:
            pile.show_top()
        self.foundations = foundations
        for pile in self.foundations:
            pile.show()

    def stock_to_tableau(self, position):
        card = self.stock.cards[-1]
        if self.tableau[position].is_valid(card):
            self.tableau[position].append(card)
            self.stock.remove(card)
            return True
        else:
            return False

    def stock_to_foundation(self, position):
        card = self.stock.cards[-1]
        self.foundations[position].append(card)
        self.stock.remove(card)

    def foundation_to_tableau(self, position_f, position_t):
        card = self.foundations[position_f].cards[-1]
        self.tableau[position_t].append(card)
        self.foundations[position_f].remove(card)

    def display(self):
        print "\nTableau"
        for pile in self.tableau:
            pile.show_top()            
            pile.display()
            print

        print "\nFoundations"
        for pile in self.foundations:
            pile.display()
            print

        self.stock.show_top()
        print "\nStock:",
        self.stock.display()
        print "\n"


def main():
    suits = ["clubs","spades","hearts","diamonds"]
    deck = Pile([])
    for suit in suits:
        for n in range(13):
            deck.append(Card(n+1, 5 * (int(n/10) + 1), suit, True))

    deck.shuffle()

    tableau = []
    for i in range(4):
        temp_card = deck.search_number(i+1)
        tableau.append(Pile([temp_card]))
        deck.remove(temp_card)

    foundations = []
    for i in range(4):
        foundations.append(Pile([]))

    table = Layout(deck,tableau, foundations)

    table.display()

if __name__ == "__main__":
    main()
