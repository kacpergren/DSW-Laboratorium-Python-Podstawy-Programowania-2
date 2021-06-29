def romanski(liczba):
   wskazniki={1:"I", 4:"IV", 5:"V", 9: "IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
   wynik=""
   for wartosc, wskaznik in sorted(wskazniki.items(), reverse=True):
      while liczba >= wartosc:
          wynik += wskaznik
          liczba -= wartosc
   return wynik

a = int(input("Podaj liczbe, ktora chcesz wymienic: "))
print("Wynik to", romanski(a))