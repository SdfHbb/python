# Funktion zur Berechnung des Durchschnitts
def durchschnitt_berechnen(name, noten):
  summe = sum(noten)
  durchschnitt = summe / len(noten)
  return name, durchschnitt

# Funktion zur Ausgabe der Durchschnittspunktzahl für jeden Schüler
def durchschnitt_ausgeben(notenliste):
  for schueler, noten in notenliste:
    name, durchschnitt = durchschnitt_berechnen(schueler, noten)
    print(f"{name}: Durchschnitt = {durchschnitt:.2f}")
# Hauptprogramm
schueler_noten = \
  [
    ("Max", [85, 90, 92]),
    ("Anna", [88, 89, 90]),
    ("Tom", [78, 80, 82]),
  ]

durchschnitt_ausgeben(schueler_noten)