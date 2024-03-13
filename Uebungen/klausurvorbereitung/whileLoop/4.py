import random

zufall = random.choice(range(1,101))
print(zufall)

while True:
  zahl = int(input("zahl raten"))
  if zahl == zufall:
    print("Erfolg")
    break
  elif zahl < zufall:
    print("Eingabezahl zu klein")
  else:
    print("Eingabezahl zu gross")