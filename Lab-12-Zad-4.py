def kilometry(a):
   wynik = a / 1000
   return wynik


wysokosc = int(input("Na jakiej wysokosci lecimy? [w metrach]: "))

liczba = kilometry(wysokosc)

if liczba > 5:
   print("Na tej wysokosci jestes juz bezpieczny")
else:
   print(liczba, "km to za nisko!")