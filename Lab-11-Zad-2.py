temperatura = int(input('Podaj temperature wody w Fahrenheitach: '))

if temperatura <= 32:
   print("Woda zamarzlaa")
if temperatura >= 212:
   print("Woda wyparowala")
else:
   print("Woda jest w stanie ciekłym")

# funkcje (trzeba by bylo dodac zmienne, ale wiadomo o co chodzi)
# k_na_f = 1.8 x temperatura_kelwiny - 459,67
# f_na_k = ((temepratura - 32)/1.8) + 273.15
# k_na_c = temperatura_kelwiny - 273.15
# c_na_k = temperatura_celecjusze + 273.15
