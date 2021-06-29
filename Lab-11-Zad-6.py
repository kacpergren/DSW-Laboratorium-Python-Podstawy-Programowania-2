liczba = int(input("Podaj liczbe ktora chce przekonwertowac: "))
binarna = bin(liczba)
osemkowa = oct(liczba)
szesnastkowa = hex(liczba)

print("Liczba w systemie binarnym to:", binarna, ",osemkowym:", osemkowa, "oraz w szesnaskowym", szesnastkowa)

# funkcje odpowiadajace za konwersje to bin() - binarny, oct() - osemkowy, hex() - szesnastkowy
