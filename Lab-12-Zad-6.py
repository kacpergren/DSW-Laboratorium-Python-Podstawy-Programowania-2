def kalkulator1(liczba):
   wynik = f'(Liczba w systemie binarnym wynosi {bin(liczba)}, a w systemie szesnastkowym {hex(liczba)}'
   return wynik

def kalkulator2(binarna):
   liczba = int(binarna, 2)
   wynik = hex(liczba)
   return wynik

def kalkulator2(szesnastkowa):
   liczba = int(szesnastkowa, base=16)
   wynik = bin(liczba)
   return wynik

def kalkulator4(liczba):
   wynik = f'(Liczba w systemie binarnym wynosi {bin(liczba)}, a w systemie osemkowym {oct(liczba)} oraz w systemie szesnastkowym {hex(liczba)}'
   return wynik
