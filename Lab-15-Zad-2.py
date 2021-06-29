class Beer:

   def __init__(self, nazwa, kategoria, stezenie_procentowe, cena, miejsce_na_opinie):
       self.nazwa = nazwa
       self.kategoria = kategoria
       self.stezenie_procentowe = stezenie_procentowe
       self.cena = cena
       self.miejsce_na_opinie = miejsce_na_opinie

   def wypisz(self):
       print(self.nazwa, "to piwo", self.kategoria, "o stezniu procentowym:", self.stezenie_procentowe, ". Jego cena to:", self.cena)

   def opinia(self):
       print(self.miejsce_na_opinie, "- to Twoja opinia o tym piwie!")

class Perla(Beer):

   def __init__(self, kategoria, stezenie_procentowa, cena, miejsce_na_opinie, nota):
       super().__init__("perla", kategoria, stezenie_procentowa, cena, miejsce_na_opinie)
       self.nota = nota

   def notka(self):
       print("Twoja nota 1-10 tego piwa to:", self.nota)

class Desperados(Beer):

   def __init__(self, kategoria, stezenie_procentowa, cena, miejsce_na_opinie, nota):
       super().__init__("desperados", kategoria, stezenie_procentowa, cena, miejsce_na_opinie)
       self.nota = nota

   def notka(self):
       print("Twoja nota 1-10 tego piwa to:", self.nota)

class Harnas(Beer):

   def __init__(self, kategoria, stezenie_procentowa, cena, miejsce_na_opinie, nota):
       super().__init__("harnas", kategoria, stezenie_procentowa, cena, miejsce_na_opinie)
       self.nota = nota

   def notka(self):
       print("Twoja nota 1-10 tego piwa to:", self.nota)


class Sklep(Beer):

   def __init__(self, kategoria, stezenie_procentowe, cena, miejsce_na_opinie):
       super().__init__("W biedronce", kategoria, stezenie_procentowe, cena, miejsce_na_opinie)

   def opis(self):
       print(self.nazwa, "znajdziejsz najlepsze piwa na naszym dziale", self.kategoria, "w promocyjnie cenie", self.cena, "za 5 takich samych piw o stezeniu procentowym:", self.stezenie_procentowe, ".")


piwska = {}
piwskalista = []

o1 = f"{input('Podaj swoja slonwa opinie o piwie Perla: ')}"
n1 = f"{int(input('Podaj swoja opinie w skali 1 do 10 o piwie Perla: '))}"
piwska["Perla"] = n1
piwskalista.append('Perla')
perla = Perla("ciemne", "5.6%", "4.99 PLN", o1, n1)

o2 = f"{input('Podaj swoja slonwa opinie o piwie Desperados: ')}"
n2 = f"{int(input('Podaj swoja opinie w skali 1 do 10 o piwie Desperados: '))}"
piwska["Desperados"] = n2
piwskalista.append('Desperados')
desperados = Desperados("smakowe", "6%", "5.99 PLN", o2, n2)

o3 = f"{input('Podaj swoja slonwa opinie o piwie Harnas: ')}"
n3 = f"{int(input('Podaj swoja opinie w skali 1 do 10 o piwie Harnas: '))}"
piwska["Harnas"] = n3
piwskalista.append('Harnas')
harnas = Harnas("ciemne", "6%", "1.99 PLN", o3, n3)

sklep = Sklep("alkoholowym", "5%", "11.99 PLN", "mila atmosfera")

posortowanepiwska = sorted(piwskalista)

print("Oceny piwa w skali do 10 punktow:", dict(sorted(piwska.items(), key=lambda item: item[1])))
print("Posortowane piwa:", posortowanepiwska)

perla.wypisz()
perla.opinia()
perla.notka()

desperados.wypisz()
desperados.opinia()
desperados.notka()

harnas.wypisz()
harnas.opinia()
harnas.notka()

sklep.opis()
