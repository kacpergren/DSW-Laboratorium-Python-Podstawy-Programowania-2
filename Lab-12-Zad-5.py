def BMI(a, b):
   wynik = a/(b*b)
   return wynik


waga = float(input("Podaj swoja wage [w kilogramach]: "))
wzrost = float(input("Podaj swoj wzrost [w metrach]: "))

liczba = BMI(waga, wzrost)

if liczba < 18.5:
   print("Masz niedowage")
elif 18.5 < liczba < 24.99:
   print("Twoja waga jest prawidlowa")
else:
   print("Masz nadwage!!!")