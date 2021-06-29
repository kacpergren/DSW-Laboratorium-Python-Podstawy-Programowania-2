class Zwierze:

   def __init__(self, gatunek, szybkosc, dzwiek):
       self.gatunek = gatunek
       self.szybkosc = szybkosc
       self.dzwiek = dzwiek

   def polowanie(self):
       print("Tu", self.gatunek, ". Jestem bardzo szybki, biegam z predkoscia", self.szybkosc, ",robię", {self.dzwiek}, "i lece na polowanie")

   def __del__(self):
       print(self.gatunek, "zostal upolowany przez kłusownikow")

class Kot (Zwierze):

   def __init__(self, szybkosc, dzwiek):
       super().__init__("garfield", szybkosc, dzwiek)

   def zycie(self):
       print("Tu", self.gatunek, ". Mam 9 zyc.")

class Pies (Zwierze):

   def __init__(self, szybkosc, dzwiek):
       super().__init__("duffy", szybkosc, dzwiek)

   def zabawka(self):
       print("Tu", self.gatunek, ". Jestem bardzo glupiutki i ciagle biegam za zabawkami")

   def spac(self):
       print("Tu", self.gatunek, ". Jestem bardzo leniwy. Mam ochote tylko spac caly dzien")

class Ptak (Zwierze):

   def __init__(self, szybkosc, dzwiek):
       super().__init__("flappy", szybkosc, dzwiek)

   def latanie(self):
       print("Tu", self.gatunek, ". Potrafie latac, a inni nie.")

class Ryba (Zwierze):

   def __init__(self, szybkosc, dzwiek):
       super().__init__("mobby", szybkosc, dzwiek)

   def plywanie(self):
       print("Tu", self.gatunek, ". Potrafie plywac, a inni nie.")

   def woda(self):
       print("Tu", self.gatunek, ". Cale zycie pije wode, mozna oszalec.")


garfield = Kot(100, "MIAU MIAU")
garfield.polowanie()
garfield.zycie()
del garfield

duffy = Pies(150, "HAU HAU")
duffy.polowanie()
duffy.zabawka()
duffy.spac()
del duffy

flappy = Ptak(125, "FIU FIU")
flappy.polowanie()
flappy.latanie()
del flappy

mobby = Ryba(50, "GUL GUL")
mobby.polowanie()
mobby.plywanie()
del mobby