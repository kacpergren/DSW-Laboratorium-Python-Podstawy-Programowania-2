# input inwokacja.txt:

#I (tekst wyswietla sie tak jak w pliku)
f = open("inwokacja.txt", 'r')
print(f.read())

# II (tekst wyswietla sie tak jak w pliku)

with open("inwokacja.txt") as plik:
   for linia in plik:
       print (linia.strip())

# III (tekst wywielta sie w postaci list)

with open("inwokacja.txt") as plik:
   for linia in plik:
       print (linia.split())

# Najlepsza opcja:

with open("inwokacja.txt") as plik:
   for linia in plik:
       print (linia.strip())
