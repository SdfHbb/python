meine_liste = []
meine_liste.extend([1, 2, 3, "Hallo"])

print(meine_liste[0])
print(meine_liste[len(meine_liste) - 1])
# print(meine_liste[- 1])

meine_liste2 = [4, 5, 6]
meine_liste += meine_liste2
print(meine_liste)

meine_liste.pop(2)
meine_liste.remove("Hallo")
print(meine_liste)

zahlen = [1, 2, 3, 4, 5]
umgekehrte_liste = zahlen[::-1]
print(umgekehrte_liste)
