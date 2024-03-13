def quadriere(zahl):
  return print(f"{zahl}² ➡️ {pow(zahl, 2)}")


def verdopple(zahl):
  return print(f"2 * {zahl} ➡️ {pow(zahl, 2)}")


def quadriere_und_verdopple(zahl):
  quadriere(zahl)
  verdopple(zahl)


quadriere_und_verdopple(5)