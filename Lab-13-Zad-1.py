class Car:

   vehicle = "samochod"

   def __init__(self, marka, model, kolor, rodzaj, wartosc):
       self.brand = marka
       self.model = model
       self.color = kolor
       self.type = rodzaj
       self.value = wartosc

   def voice(self, horn):
       return"{} ma klakson {}".format(self.brand, horn)

   def jedzprosto(self):
       return"{} jedzie prosto".format(self.brand)

   def redlight(self):
       return"{} zatrzymuje się z piskiem opon na czerwonym".format(self.brand)

   def speed(self, counter):
       return"{} zamyka liczniki predkoscia {}".format(self.brand, counter)

   def dirty(self):
       return"{} ubrudzil sie od wysokich predkosci".format(self.brand)


ferrari = Car("Ferrari", "812 GTS", "czerwone", "kabriolet", 60000)
lamborghini = Car("Lamborghini", "Aventador SVJ", "zolte", "kabriolet", 2000000)
bmw = Car("BMW", "M3 Competition", "niebieskie", "sedan", 450000)
mercedes = Car("Mercedes", "SL 500", "szare", "kabriolet", 550000)
lexus = Car("Lexus", "LC 500", "czarne", "sedan", 350000)