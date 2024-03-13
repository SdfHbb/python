# Dictionary initialisieren
woerterbuch = {}

# Funktion zum Anzeigen des Wörterbuchs
def woerterbuch_anzeigen():
  print("Wörterbuch:")
  for deutsch, englisch in woerterbuch.items():
    print(f"{deutsch}: {englisch}")

# Funktion zum Hinzufügen eines Worts zum Wörterbuch
def wort_hinzufuegen():
  deutsch = input("Gib das deutsche Wort ein: ")
  englisch = input("Gib die englische Übersetzung ein: ")
  woerterbuch[deutsch] = englisch
  print(f"{deutsch} wurde dem Wörterbuch hinzugefügt.")
# Funktion zum Löschen eines Worts aus dem Wörterbuch

def wort_loeschen():
  deutsch = input("Gib das deutsche Wort ein, das du löschen möchtest: ")
  if deutsch in woerterbuch:
    del woerterbuch[deutsch]
    print(f"{deutsch} wurde aus dem Wörterbuch gelöscht.")
  else:
    print(f"{deutsch} wurde nicht im Wörterbuch gefunden.")

# Funktion zum Übersetzen eines Worts
def wort_uebersetzen():
  deutsch = input("Gib das deutsche Wort ein, das du übersetzen möchtest: ")
  if deutsch in woerterbuch:
    print(f"{deutsch} wird auf Englisch als {woerterbuch[deutsch]} übersetzt.")
  else:
    print(f"{deutsch} wurde nicht im Wörterbuch gefunden.")

# Hauptprogrammschleife
while True:
  print("\nWähle eine Aktion:")
  print("1. Wörterbuch anzeigen")
  print("2. Wort hinzufügen")
  print("3. Wort löschen")
  print("4. Wort übersetzen")
  print("5. Beenden")

  auswahl = input("Gib die Nummer der gewünschten Aktion ein: ")

  if auswahl == "1":
    woerterbuch_anzeigen()
  elif auswahl == "2":
    wort_hinzufuegen()
  elif auswahl == "3":
    wort_loeschen()
  elif auswahl == "4":
    wort_uebersetzen()
  elif auswahl == "5":
    print("Programm wird beendet.")
    break
  else:
    print("Ungültige Eingabe. Bitte wähle eine gültige Aktion.")

