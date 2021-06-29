jednostka = f"{input('Wybierz jedna z podanych jednostek: stopy, cale, lokcie, lawki. Wybrana: ')}"
wysokosc = float(input("Podaj wysokosc: "))

if jednostka == "stopy":
   metry = wysokosc/3.280840
   centymetry = metry*100
   milimetry = centymetry*10
   kilometry = metry/1000
   print("Wysokosc wynosi", metry, "metrow,", centymetry, "centymetrow,", milimetry, "milimetrow oraz", kilometry, "kilometrow.")
if jednostka == "cale":
   metry = wysokosc/39.37
   centymetry = metry*100
   milimetry = centymetry*10
   kilometry = metry/1000
   print("Wysokosc wynosi", metry, "metrow,", centymetry, "centymetrow,", milimetry, "milimetrow oraz", kilometry, "kilometrow.")
if jednostka == "lokcie":
   metry = wysokosc/1.72
   centymetry = metry*100
   milimetry = centymetry*10
   kilometry = metry/1000
   print("Wysokosc wynosi", metry, "metrow,", centymetry, "centymetrow,", milimetry, "milimetrow oraz", kilometry, "kilometrow.")
if jednostka == "lawki":
   metry = wysokosc/22.42
   centymetry = metry*100
   milimetry = centymetry*10
   kilometry = metry/1000
   print("Wysokosc wynosi", metry, "metrow,", centymetry, "centymetrow,", milimetry, "milimetrow oraz", kilometry, "kilometrow.")
