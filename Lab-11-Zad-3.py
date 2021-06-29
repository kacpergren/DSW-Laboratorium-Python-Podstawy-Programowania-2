import math

kat = int(input("Wybierz jedna z podanych wartosci kata: 35, 70, 90, 180, 240, 360. Wybrana: "))
sinus = float(math.sin(kat))
cosinus = float(math.cos(kat))
tangens = f'{math.tan(kat)}'

if kat <= 70:
   cotangens = f'{cosinus / sinus}'
   print(f"Sinus wynosi: {sinus}, cosinus: {cosinus}, tangens: {tangens} oraz cotangens: {cotangens}")
if kat == 90:
   cotangens = f'{cosinus / sinus}'
   print(f"Sinus wynosi: {sinus}, cosinus: {cosinus}, tangens: Brak tangensa! oraz cotangens: {cotangens}")
if kat == 180:
   print(f"Sinus wynosi: {sinus}, cosinus: {cosinus}, tangens: {tangens} oraz cotangens: Brak cotangensa!")
if kat == 240:
   cotangens = f'{cosinus / sinus}'
   print(f"Sinus wynosi: {sinus}, cosinus: {cosinus}, tangens: {tangens} oraz cotangens: {cotangens}")
if kat == 360:
   print(f"Sinus wynosi: {sinus}, cosinus: {cosinus}, tangens: {tangens} oraz cotangens: Brak cotangensa!")