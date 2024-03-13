# 1
def summe(zahl):
  sum = 0
  for i in range(1, zahl + 1):
    sum += i
  return sum


print(summe(5))


# 2
def summe_list(*args):
  sum = 0
  for zahl in args[0]:
    if zahl % 2 == 1:
      sum += zahl
  return sum


zahlen_beispiel = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(summe_list(zahlen_beispiel))


# 3

satz = "Python ist eine großartige Programmiersprache"
def wortlaengen_dict(satz):
  wortlaengen = {}
  woerter = satz.split()
  for wort in woerter:
    wortlaengen[wort] = len(wort)
  return wortlaengen

# Beispielaufruf:
satz = "Python ist eine großartige Programmiersprache"
wortlaengen_resultat = wortlaengen_dict(satz)
print(wortlaengen_resultat)


# 3 alternativ

def woerter_zaehlen(satz):
  woerter = satz.split()
  return len(woerter)


anzahl_woerter = woerter_zaehlen("Python ist eine Programmiersprache")
print(anzahl_woerter)

# 4

def schachbrett_muster(n):
  muster = ""
  for i in range(n):
    for j in range(n):
      if (i + j) % 2 == 0:
        muster += "#"
      else:
        muster += " "
    muster += "\n"
  return muster

# Beispielaufruf:
resultat_muster = schachbrett_muster(5)
print(resultat_muster)