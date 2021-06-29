import random
i = 0
result = 0

liczba = int(input("Podaj liczbe koncowa: "))
wylosowana = random.randrange(liczba)
print(wylosowana)

if wylosowana < 0:
   print("Sprobuj jeszcze raz, wylosowana nie moze byc mniejsza od zera")
else:
   for i in range(1,wylosowana+1):
       result = result + (i*i)
   print("Suma kwadratow wynosi:", result)

# tak matematyka jest niezbedna programiscie!!!
