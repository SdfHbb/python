set1 = {1, 2, 3}
set2 = {4, 5, 6, 7, 8}
set3 = set(())

is_set1_empty = not bool(set1)
set2.difference_update({x for x in set2 if x > 5})
print("Ist set1 leer?", is_set1_empty)
print("set2 nach der Entfernung von Elementen größer als 5:", set2)
