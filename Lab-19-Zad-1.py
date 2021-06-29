while 1:
   try:
       x = int(input("Proszę wprowadzić liczbę: "))
       if 10000 < x < 99999:
           file1 = open("kody.txt, w")
           file1.write(f"{x}")
           file1.close()
           print(True)
       else:
           print(False)
   except ValueError:
       print("To nie jest liczba")

# na potrzeby programu stworzylem pusty plik kody.txt
