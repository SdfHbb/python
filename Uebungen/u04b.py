# 1️⃣
def summe(zahl):
  result = 0
  zaehler = zahl
  while zaehler > 0:
    result += zaehler
    zaehler -= 1
  return print(f"1️⃣ Die Summe von 1 bis {zahl} ➡️ {result}")

summe(5)

# 2️⃣
def anzahl_stellen(zahl):
  zahl1 = zahl
  result = 0
  while zahl1 > 0:
    zahl1 //= 10
    result += 1
  return print(f"1️⃣ Die Zahl {zahl} hat ➡️ {result} Stellen")

anzahl_stellen(12345)

# 3️⃣
def fakultaet(zahl):
  zahl1 = zahl
  result = 1
  while zahl1 > 0:
    result *= zahl1
    zahl1 -= 1
  return print(f"1️⃣ Die Fakultät von {zahl} ist ➡️ {result}")

fakultaet(5)