class Student:

   def __init__(self, uczelnia, tryb, pora):
       self.school = uczelnia
       self.type = tryb
       self.part = pora

   def angry(self, emotions):
       return"Studia {} w trybie {} są do {}!!!".format(self.part, self.type, emotions)

   def practice(self, business):
       return"{} zalatwilo mi wymarzone praktyki w {}!!!".format(self.school, business)

janek = Student("DSW", "stacjonarnym", "dzienne")
marcin = Student("DSW", "niestacjonarnym", "wieczorowe")
kamil = Student("DSW", "stacjonarnym", "wieczorowe")

print("Student studiuje w trybie {}, {} na uczelni {}".format(janek.type, janek.part, janek.school))

print(janek.angry("'BANII"))
print(janek.practice("'DELOITTE'"))