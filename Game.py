from Card import Card
from Pile import Pile, Tableau
from Layout import Layout

import os,subprocess
def clear():
    if os.name in ('nt','dos'):
        subprocess.call("cls")
    elif os.name in ('linux','osx','posix'):
        subprocess.call("clear")
    else:
        print "\n"*120

class Game:
    def __init__(self):
        suits = ["clubs","spades","hearts","diamonds"]
        deck = Pile([])
        for suit in suits:
            for n in range(13):
                deck.append(Card(n+1, 5 * int(n/10), suit, True))

        deck.shuffle()
        deck.show_top()

        tableau = []
        for i in range(4):
            temp_card = deck.search_number(i+1)
            tableau.append(Tableau(i+1, [temp_card]))
            deck.remove(temp_card)

        foundations = []
        for i in range(4):
            foundations.append(Pile([]))

        self.table = Layout(deck,tableau, foundations)

    def move(self, num1, num2):
        if num1 == 0:
            card = self.table.stock.cards[-1]
            if not self.table.stock_to_tableau(num2-1):
                self.table.stock_to_foundation(num2-1)
            return True
        else:
            if self.table.tableau[num2].is_valid(self.table.foundations[num1].cards[-1]):
                return self.table.foundation_to_tableau(num1,num2-1)

    def play(self):
        quit = False
        move_number = 1
        clear()
        while not quit:
            print "Calculation\nMove: %d" % move_number
            self.table.display()
            try:
                num1 = raw_input("Enter origin: ")
                if num1 == "quit":
                    break
                num2 = raw_input("Enter destination: ")
                self.move(int(num1), int(num2))
                move_number += 1
            except:
                print "Exception"
            clear()


def main():
    game = Game()
    game.play()

if __name__ == "__main__":
    main()
