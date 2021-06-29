class Book:

   def __init__(self, autor, tytul, kolor, rodzaj, ilosc_stron):
       self.author = autor
       self.title = tytul
       self.color = kolor
       self.type = rodzaj
       self.number = ilosc_stron

   def czytaj(self):
       return"Czytam {}".format(self.title)

   def lenght(self):
       return"Ksiazka {} ma az {} stron!!!".format(self.title, self.number)

   def school(self):
       return"{} autorstwa {} znajduje sie w szkolnej bibliotece".format(self.title, self.author)

   def shop(self):
       return"Ksiazka {} znajduje sie na dziale {}".format(self.title, self.type)

   def voice(self, word):
       return"Moja recenzja tej nowej ksiazki, {} to {}".format(self.title, word)


parasol = Book("Stephen King", "Parasol", "czerwona", "horror", 600)
mercedes = Book("Stephen King", "Mercedes", "zolta", "horror", 200)
lsnienie = Book("Stephen King", "Lsnienie", "niebieska", "horror", 450)
koddavinci = Book("Dan Brown", "Kod da Vinci", "szara", "horror", 550)
aniolyidemony = Book("Dan Brown", "Anioly i Demony", "czarna", "horror", 350)

print("Ksiazka autorstwa {}, {} to nowy {}".format(lsnienie.title, lsnienie.author, lsnienie.type))
print("{} ksiazka ma okolo {} stron".format(lsnienie.color, lsnienie.number))

print(lsnienie.czytaj())
print(lsnienie.voice("'Straszna'"))