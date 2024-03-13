# 1.1. Erstellen Sie eine leere Liste mit dem Namen meine_liste.
meine_liste = []
# 1.2. Fügen Sie die Zeichenfolgen "Apfel", "Banane" und "Orange" der Liste hinzu.
meine_liste.extend(["Apfel", "Banane", "Orange"])

# 2.1. Geben Sie das zweite Element der Liste meine_liste aus.
print("Zweites Element:", meine_liste[1])
# 2.2. Geben Sie die Liste in umgekehrter Reihenfolge aus.
print("Liste in umgekehrter Reihenfolge:", meine_liste[::-1])

# 3.1. Erstellen Sie eine neue Liste namens zusatz_liste mit den Elementen "Erdbeere" und "Traube".
zusatz_liste = ["Erdbeere", "Traube"]
# 3.2. Verketten Sie meine_liste und zusatz_liste in einer neuen Liste namens kombinierte_liste.
kombinierte_liste = meine_liste + zusatz_liste
print(kombinierte_liste)

# 4.1. Entfernen Sie das Element "Banane" aus kombinierte_liste.
kombinierte_liste.remove("Banane")
print(kombinierte_liste)
# 4.2. Entfernen Sie das erste Element von meine_liste.
del meine_liste[0]
print(meine_liste)

# 5.1. Überprüfen Sie, ob "Apfel" in meine_liste vorhanden ist.
ist_vorhanden = "Apfel" in meine_liste
print(ist_vorhanden)
# 5.2. Finden Sie den Index des Elements "Orange" in meine_liste.
print(kombinierte_liste.index("Orange"))

# 6.1. Sortieren Sie kombinierte_liste in aufsteigender Reihenfolge.
kombinierte_liste.sort()
print(kombinierte_liste)
# 6.2. Sortieren Sie meine_liste in absteigender Reihenfolge.
kombinierte_liste.sort(reverse=True)
print(kombinierte_liste)
