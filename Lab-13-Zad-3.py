class Smartphone:

   def __init__(self, marka, model, cena):
       self.brand = marka
       self.model = model
       self.price = cena

   def aparat(self, assessment):
       return"Telefon {} ma {} aparat!!!".format(self.brand, assessment)

   def glass(self):
       return"Cholera, wlasnie sltuklem szybe w moim nowym {} !!!".format(self.model)

   def thief(self):
       return"Prosze, oddaj mi ten telefon!!! Zaplacilem za niego {}".format(self.price)

samsung = Smartphone("Samsung", "S10+", 6000)
iphone = Smartphone("IPhone", "6S", 2000)
xiaomi = Smartphone("Xiaomi", "MI10", 450)

print("Nowy telefon {}, {} to swiatowy bestseller".format(samsung.brand, samsung.model))
print("Ten telefon kosztowal mnie {} polskich zlotowek :(".format(samsung.price))

print(samsung.glass())
print(samsung.aparat("'KOZACKI'"))