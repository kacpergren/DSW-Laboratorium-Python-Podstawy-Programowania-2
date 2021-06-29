def Palindrom(s):
   return s == s[::-1]

s = (input('Podaj wyraz, do sprawdzenia czy jest palindromem: '))
ans = Palindrom(s)

if ans:
   print("Tak, jest palindromem")
else:
   print("Nie, nie jest palindromem")

# test_first.py

def Palindrom(s):
   return s == s[::-1]

def test_Palindrom():
   x = "kayak"
   assert Palindrom(x) == True

def test_Palindrom_fail():
   assert Palindrom("kaczka") == "kaczka"


# opdalam pytest w konsoli
