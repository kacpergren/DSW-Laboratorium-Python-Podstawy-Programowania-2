import linecache

wiersz1 = linecache.getline("inwokacja.txt", 8)
wiersz2 = linecache.getline("inwokacja.txt", 12)
wiersz3 = linecache.getline("inwokacja.txt", 60)
wiersz4 = linecache.getline("inwokacja.txt", 98)
wiersz5 = linecache.getline("inwokacja.txt", 104)

print(wiersz1)
print(wiersz2)
print(wiersz3)
print(wiersz4)
print(wiersz5)

count = -1
for count, wiersza in enumerate(open("inwokacja.txt", 'r')):
   pass
count += 1
print("Inwokacja ma tak ilosc wierszy:", count)

# wierze wyswietlaja sie poprawnie do 2 - inwokacja ma 40 wierszy