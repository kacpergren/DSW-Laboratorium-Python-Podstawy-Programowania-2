class Obywatel:

   imie = None
   nazwisko = None
   ulica = None
   nr_domu = None
   kod_pocztowy = None
   miejscowosc = None

   def __init__(self, imie, nazwisko, ulica, nr_domu, kod_pocztowy, miejscowosc):
       self.imie = imie
       self.nazwisko = nazwisko
       self.ulica = ulica
       self.nr_domu = nr_domu
       self.kod_pocztowy = kod_pocztowy
       self.miejscowosc = miejscowosc

   def wypisz(self):
       print(f"{self.imie} {self.nazwisko} \n{self.ulica} {self.nr_domu} \n{self.kod_pocztowy} {self.miejscowosc}")

file1 = open("wizytowka.txt", "w")

i = f"{input('Podaj imie:')}"
n = f"{input('Podaj nazwisko:')}"
u = f"{input('Podaj ulice:')}"
nr = f"{input('Podaj numer:')}"
k = f"{input('Podaj kod pocztowy:')}"
m = f"{input('Podaj miejscowosc:')}"
obywatel = Obywatel(  i, n, u, nr, k, m)
obywatel.wypisz()
file1.write(f"{obywatel.imie} {obywatel.nazwisko} \n{obywatel.ulica} {obywatel.nr_domu} \n{obywatel.kod_pocztowy} {obywatel.miejscowosc}")
file1.close()

# na potrzeby programu stworzylem pusty plik wizytowka.txt
