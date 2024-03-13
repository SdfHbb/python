def doppel(zahl):
  return print(f"2 * {zahl} ➡️ {2 * zahl}")

doppel(5)

def ist_gerade(zahl):
  if zahl % 2 == 0:
    return print(f"{zahl} ist eine gerade Zahl")
  else:
    return print(f"{zahl} ist keine gerade Zahl")

ist_gerade(5)

def summe_bis(zahl):
  zaehler = 1
  summe = 0
  while zaehler <= zahl:
    summe += zaehler
    zaehler += 1
  return print(f"Die Summe von 1 bis {zahl} ➡️ {summe}")

summe_bis(10)

def quadrat(zahl):
  return print(f"Das Quadrat von {zahl} ➡️ {pow(zahl, 2)}")

quadrat(4)

def mittlere_zahl(zahl1, zahl2, zahl3):
  my_list = [zahl1, zahl2, zahl3]
  my_list.sort()
  return print(f"Mittlere Zahl von {zahl1}  {zahl2}  {zahl3} ➡️ {my_list[1]} ")

mittlere_zahl(3, 4, 5)
