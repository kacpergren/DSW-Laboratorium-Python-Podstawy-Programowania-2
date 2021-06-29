def suma(x, y):
   c = x + y
   return c

def odejmowanie(x, y):
   c = x - y
   return c

def mnozenie(x, y):
   c = x * y
   return c

def dzielenie(x, y):
   if(y==0):
       return
   else:
       return x / y

def potegowanie(x):
   return x*x

print("Suma wynosi: ", suma(1, 4))
print("Odejmowanie wynosi: ", odejmowanie(1, 4))
print("Mnozenie wynosi: ", mnozenie(1, 4))
print("Dzielenie wynosi: ", dzielenie(1, 4))
print("Potega a wynosi: ", potegowanie(1))
print("Potega b wynosi: ", potegowanie(4))
