set1 = {1, 2, 3, 4, 5}
set2 = set((4, 5, 6, 7, 8))

set1.add(11)
print(f"Add '11' zu sets ➡️ {set1}")

print(f"Ist '10' in set2 vorhanden ➡️ {11 in set2}")

set1.remove(1)
print(f"#4 Element 5 wurde entfernt ➡️ {set1}")
