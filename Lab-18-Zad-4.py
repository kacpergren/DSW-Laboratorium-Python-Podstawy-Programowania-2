from timer import Timer
t = Timer()
t.start()

def kopcowanie(arr, n, i):
   najwieksza = i
   l = 2 * i + 1
   r = 2 * i + 2

   if l < n and arr[najwieksza] < arr[l]:
       najwieksza = l

   if r < n and arr[najwieksza] < arr[r]:
       largest = r

   if najwieksza != i:
       arr[i], arr[najwieksza] = arr[najwieksza], arr[i]  # swap

       kopcowanie(arr, n, najwieksza)

def sortowaniekopcowe(arr):
   n = len(arr)

   for i in range(n // 2 - 1, -1, -1):
       kopcowanie(arr, n, i)

   for i in range(n - 1, 0, -1):
       arr[i], arr[0] = arr[0], arr[i]  # swap
       kopcowanie(arr, i, 0)

arr = [4, 10, 11, 5, 73, 5, 1]
sortowaniekopcowe(arr)
n = len(arr)
print("Posortowane liczby to: ")
for i in range(n):
   print("%d" % arr[i]),

t.stop()

# b)

from timer import Timer
t = Timer()
t.start()

def przegroda(arr, niska, wysoka):
   i = (niska - 1)
   os = arr[wysoka]

   for j in range(niska, wysoka):

       if arr[j] <= os:
           i = i + 1
           arr[i], arr[j] = arr[j], arr[i]

   arr[i + 1], arr[wysoka] = arr[wysoka], arr[i + 1]
   return (i + 1)

def quickSort(arr, niska, wysoka):
   if len(arr) == 1:
       return arr
   if niska < wysoka:
       pi = przegroda(arr, niska, wysoka)

       quickSort(arr, niska, pi - 1)
       quickSort(arr, pi + 1, wysoka)

arr = [4, 10, 11, 5, 73, 5, 1]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
   print("%d" % arr[i]),

t.stop()

# czasy wykonowania algorytmu sa takie same i wynosza 0.0001s, wynika to z malej ilosci liczb

# c)

# Tablice mozemy wczytac z pliku za pomoca:

file = open("tablica.txt", "r")
lines = file.read().split(',')

# I potem podmieniamy tablice w kodach na “lines”

# Oczywiscie samo wczytywanie z pliku znacznie wydłuży wykonywanie sie programu w zaleznosci od ilosci podanych zmiennych

# d)

# Musiałbym wpisać wartość “nieskończoność” do pliku. Algorytmy beda sie wykonywac nawet dla bardzo duzej ilosci liczb, ale ich praca moze trwac bardzo dlugo.