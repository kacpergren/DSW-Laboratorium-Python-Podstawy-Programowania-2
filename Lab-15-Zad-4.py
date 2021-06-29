from random import shuffle


class Card:
   suits = ["pik",
            "serce",
            "kier",
            "trefl"]

   values = [None, None,"2", "3",
             "4", "5", "6", "7",
             "8", "9", "10",
             "Jopek", "Krolowa",
             "Krol", "As"]

   def __init__(self, v, s):
       self.value = v
       self.suit = s

   def __lt__(self, c2):
       if self.value < c2.value:
           return True
       if self.value == c2.value:
           if self.suit < c2.suit:
               return True
           else:
               return False
       return False

   def __gt__(self, c2):
       if self.value > c2.value:
           return True
       if self.value == c2.value:
           if self.suit > c2.suit:
               return True
           else:
               return False
       return False

   def __repr__(self):
       v = self.values[self.value] +\
           " z " + \
           self.suits[self.suit]
       return v


class Deck:

   #sortowanie

   def __init__(self):
       self.cards = []
       for i in range(2, 15):
           for j in range(4):
               self.cards\
                   .append(Card(i,
                                j))
       shuffle(self.cards)

   def rm_card(self):
       if len(self.cards) == 0:
           return
       return self.cards.pop()

   #wyswietlanie

   def print(self):
       self.cards = []
       for i in range(2, 15):
           for j in range(4):
               self.cards \
                   .append(Card(i,
                                j))
       print(self.cards)

   # dodawanie

   def add(self):
       self.cards = []
       for i in range(2, 15):
           for j in range(4):
               self.cards \
                   .append(Card(i,
                                j))
       karta = input('Jaka karte chcesz dodac? np. 4 z Trefl')
       self.cards.append(f"{karta}")

   # odejmowanie

   def delete(self):
       self.cards = []
       for i in range(2, 15):
           for j in range(4):
               self.cards \
                   .append(Card(i,
                                j))
       karta = input('Jaka karte chcesz usunac? np. 4 z Trefl')
       self.cards.remove(f"{karta}")

   # insert

   def insert(self):
       self.cards = []
       for i in range(2, 15):
           for j in range(4):
               self.cards \
                   .append(Card(i,
                                j))
       print(self.cards)
       karta = input('Najpierw musisz usunac karte w pierwotnego miejsca. Podaj jej nazwe, np. 4 z Trefl:')
       self.cards.remove(f"{karta}")
       indeks = int(input('Wybierz nowy indeks dla karty:'))
       self.cards.insert(indeks, f"{karta}")

class Actions:
   def __init__(self):
       self.deck = Deck()

   def draw(self, p1c, p2c):
       d = "Wylosowane to {} {}"
       d = d.format(p1c,
                    p2c)
       print(d)

   # porowananie

   def comprasion(self):
       p1c = self.deck.rm_card()
       p2c = self.deck.rm_card()
       self.draw(p1c,p2c)
       if p1c > p2c:
           print(p1c, "jest większa od", p2c)
       elif p1c == p2c:
           print(p1c, "jest rowna", p2c)
       else:
           print(p1c, "jest mniejsza od", p2c)

class Player:
   def __init__(self, name):
       self.wins = 0
       self.card = None
       self.name = name


class Game:
   def __init__(self):
       name1 = input("Imie pierwszego gracza ")
       name2 = input("Imie drugiego gracza ")
       self.deck = Deck()
       self.p1 = Player(name1)
       self.p2 = Player(name2)

   def wins(self, winner):
       w = "{} wygrywa te runde"
       w = w.format(winner)
       print(w)

   def draw(self, p1n, p1c, p2n, p2c):
       d = "{} wylosowal {} {} wylosowal {}"
       d = d.format(p1n,
                    p1c,
                    p2n,
                    p2c)
       print(d)

   # przerobiona klasa odpowiadajaca za porownywanie
   def play_game(self):
       cards = self.deck.cards
       print("Zaczynamy wojne!")
       while len(cards) >= 2:
           m = "q zeby zakonczyc. Jakikolwiek " + \
               "przycisk zeby grac:"
           response = input(m)
           if response == 'q':
               break
           p1c = self.deck.rm_card()
           p2c = self.deck.rm_card()
           p1n = self.p1.name
           p2n = self.p2.name
           self.draw(p1n,
                     p1c,
                     p2n,
                     p2c)
           if p1c > p2c:
               self.p1.wins += 1
               self.wins(self.p1.name)
           else:
               self.p2.wins += 1
               self.wins(self.p2.name)

       win = self.winner(self.p1,
                        self.p2)
       print("Wojna skonczona.{} wygrywa"
             .format(win))

   def winner(self, p1, p2):
       if p1.wins > p2.wins:
           return p1.name
       if p1.wins < p2.wins:
           return p2.name
       return "To byl remis."

game = Game()
game.play_game()
