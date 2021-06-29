import math
from abc import ABC, abstractmethod


class Figura(ABC):
   @abstractmethod
   def nazwa(self):
       pass

   def wypisz(self):
       print(f"Jestem {self.nazwa()}. Moj obwod: {self.obwod()}, a pole: {self.pole()}.")

   @abstractmethod
   def obwod(self):
       pass

   @abstractmethod
   def pole(self):
       pass


class Trojkat(Figura):
   def __init__(self, a, b, c):
       self.a = a
       self.b = b
       self.c = c

   def nazwa(self):
       return "trojkat"

   def obwod(self):
       return self.a + self.b + self.c

   def pole(self):
       p = self.obwod()/2
       return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

class Kolo(Figura):
   def __init__(self, r):
       self.r = r

   def nazwa(self):
       return "kolo"

   def obwod(self):
       return 2 * math.pi * self.r

   def pole(self):
       return math.pi * self.r ** 2

class Kwadrat(Figura):
   def __init__(self, a):
       self.a = a

   def nazwa(self):
       return "kwadrat"

   def obwod(self):
       return 4 * self.a

   def pole(self):
       return self.a ** 2

class Prostokat(Kwadrat):
   def __init__(self, a, b):
       super().__init__(a)
       self.b = b

   def nazwa(self):
       return "prostokat"

   def obwod(self):
       return 2 * (self.a + self.b)

   def pole(self):
       return self.a * self.b

class Romb(Figura):
   def __init__(self, a, h):
       self.a = a
       self.h = h

   def nazwa(self):
       return "romb"

   def obwod(self):
       return 4 * self.a

   def pole(self):
       return self.a * self.h

class Trapez(Kwadrat):
   def __init__(self, a, b, c, h):
       super().__init__(a)
       self.b = b
       self.c = c
       self.h = h

   def nazwa(self):
       return "prostokat"

   def obwod(self):
       return self.a + self.b + self.c * 2

   def pole(self):
       return ((self.a + self.b) * self.h) / 2

wybor = input("Wubierz figure z listy: romb, prostkat, trojkat, kwadrat, kolo, trapez: ")

if wybor == "romb":
   bok1 = int(input("Podaj dlugosc boku romba: "))
   wysokosc = int(input("Podaj dlugosc wysokosci romba: "))
   r = Romb(bok1, wysokosc)
   r.wypisz()

if wybor == "prostokat":
   bok1 = int(input("Podaj dlugosc pierwszego boku prostkata: "))
   bok2 = int(input("Podaj dlugosc drugiego boku prostkata: "))
   p = Prostokat(bok1, bok2)
   p.wypisz()

if wybor == "trojkat":
   bok1 = int(input("Podaj dlugosc pierwszego boku trojkata: "))
   bok2 = int(input("Podaj dlugosc drugiego boku trojkata: "))
   bok3 = int(input("Podaj dlugosc drugiego boku trojkata: "))
   t = Trojkat(bok1, bok2, bok3)
   t.wypisz()

if wybor == "kwadrat":
   bok1 = int(input("Podaj dlugosc pierwszego boku kwadrata: "))
   k = Kwadrat(bok1)
   k.wypisz()

if wybor == "kolo":
   bok1 = int(input("Podaj dlugosc promienia kola: "))
   k = Kolo(bok1)
   k.wypisz()

if wybor == "trapez":
   bok1 = int(input("Podaj dlugosc pierwszego boku trapeza: "))
   bok2 = int(input("Podaj dlugosc drugiego boku trapeza: "))
   bok3 = int(input("Podaj dlugosc drugiego boku trapeza: "))
   wysokosc = int(input("Podaj dlugosc wysokosci trapeza: "))
   t = Trapez(bok1, bok2, bok3, wysokosc)
   t.wypisz()
