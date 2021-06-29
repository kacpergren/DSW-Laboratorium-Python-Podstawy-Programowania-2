class Resturant:

   def __init__(self, nazwa, ceny, lokalizacja):
       self.nazwa = nazwa
       self.ceny = ceny
       self.lokalizacja = lokalizacja

   def wypisz(self):
       print("Zapraszamy do naszej restauracji:", self.nazwa, ". Znajdziesz nas we Wroclawiu przy ulicy:", self.lokalizacja, "! Mamy", self.ceny, "w miescie.")

class IceCreamStand(Resturant):

   def __init__(self, ceny, lokalizacja, flavors):
       super().__init__(self, ceny, lokalizacja)
       self.flavors = flavors

   def smaki1(self):
       print("Obecnie dostepne smaki lodow to:", self.flavors)

class CoffeeShop(Resturant):

   def __init__(self, ceny, lokalizacja, flavors):
       super().__init__(self, ceny, lokalizacja)
       self.flavors = flavors

   def smaki2(self):
       print("Obecnie dostepne kawy w naszym asortymencie to:", self.flavors)

lody = IceCreamStand("niskie", "Arktycznej 5", "guma balaonowa, smerfowy, truskawkowy, krowkowy, mietowy")
lody.smaki1()

lody = CoffeeShop("wystrzalowe", "Kakaowej 18", "americano, latte, mocha latte, prazona, mala czarna")
lody.smaki2()

# program wpisuje sie w dziedziczenie, po krotkiej poprawie kodu moglby sie wpisywac w polimorfyzm. abstrakcja tez moglaby zostac tutaj uzyta, hermetyzacja moim zdaniem raczej nie ma tutaj potrzeby
