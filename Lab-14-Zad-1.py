class Pojazd:

   def __init__(self, marka, szybkosc, nr_tablicy):
       self.marka = marka
       self.szybkosc = szybkosc
       self.nr_tablicy = nr_tablicy

   def jazda(self):
       print("Tu", self.marka, ",na liczniku:", self.szybkosc, ",jade z bardzo wysoka predkoscia")

class Samochod (Pojazd):

   def __init__(self, szybkosc, nr_tablicy):
       super().__init__("ferrari", szybkosc, nr_tablicy)

   def illegal(self):
       print("Tu", self.marka, ". Zamykam licznik na czerwonym.")

   def __del__(self):
       print(self.marka, "ulegl calkowitemu zniszczeniu. Mial okropny wypadek")

class Motocykl (Pojazd):

   def __init__(self, szybkosc, nr_tablicy):
       super().__init__("harley", szybkosc, nr_tablicy)

   def flop(self):
       print("Tu", self.marka, ". Chcialem przejechac na czerwonym, ale zatrzymali mnie niebiescy panowie")

   def zima(self):
       print("Tu", self.marka, ".Jestem bezużyteczny w zimie :'(")

   def __del__(self):
       print(self.marka, "ulegl calkowitemu zniszczeniu. Mial okropny wypadek")

ferrari = Samochod(250, "RJA52020")
ferrari.jazda()
ferrari.illegal()
del ferrari

harley = Motocykl(150, "RLU75834")
harley.jazda()
harley.flop()
harley.zima()
del harley
