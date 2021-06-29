pliczek1 = input("Podaj nazwe pierwszego pliku np. ramka.txt: ")
pliczek2 = input("Podaj nazwe drugiego pliku np. ramka.txt: ")
n = 3
i = 0

f = open(pliczek1, "r")
f2 = open(pliczek2, "r")

try:

   from itertools import zip_longest

   with open(pliczek1) as f1, open(pliczek2) as f2, open("wynik.txt", 'w') as of:
       for lines in zip_longest(f1, f2):
           for line in lines:
               if line is not None: print(line.rstrip(), file=of)

   f3 = open('wynik.txt', 'r')
   print(f3.read())

except FileNotFoundError:
   print(" Blad : nie mozna odnalezc pliku lub odczytac danych ")

# na potrzeby programu stworzylem pliki polityka.txt i sport.txt z newsami oraz wynik.txt z outputem
