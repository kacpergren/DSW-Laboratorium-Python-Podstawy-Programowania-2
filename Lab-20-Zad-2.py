def kobieta(a, b, c):
    wynik = 655.1 + (9.563 * a) + (1.85 * b) - (4.676 * c)
    return wynik


def mezczyzna(a, b, c):
    wynik = 66.5 + (13.75 * a) + (5.003 * b) - (6.775 * c)
    return wynik


wybor = input("Jestes meczyzna czy kobieta? Odpowiedz: ")

if wybor == "mezczyzna":
    waga = float(input("Podaj swoja wage [w kilogramach]: "))
    wzrost = float(input("Podaj swoj wzrost [w metrach]: "))
    wiek = float(input("Podaj swoj wiek [w latach]: "))
    liczba = mezczyzna(waga, wzrost, wiek)
    print("Twoje PPM:", liczba)

if wybor == "kobieta":
    waga = float(input("Podaj swoja wage [w kilogramach]: "))
    wzrost = float(input("Podaj swoj wzrost [w metrach]: "))
    wiek = float(input("Podaj swoj wiek [w latach]: "))
    liczba = kobieta(waga, wzrost, wiek)
    print("Twoje PPM:", liczba)


# test_second.py

def kobieta(a, b, c):
    wynik = 655.1 + (9.563 * a) + (1.85 * b) - (4.676 * c)
    return wynik


def test_kobieta():
    assert kobieta(70, 1.7, 30) == 1187.3750000000002


def test_kobieta():
    assert kobieta(72, 1.8, 32) == 1187.3750000000002

# opdalam pytest w konsoli.