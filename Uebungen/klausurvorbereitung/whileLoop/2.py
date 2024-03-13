zahl = int(input("zahl bitte"))
anzahl = 0

while zahl > 0:
  zahl //= 10
  anzahl += 1

print(f"{anzahl} Stellen")