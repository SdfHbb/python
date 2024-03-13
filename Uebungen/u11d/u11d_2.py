set1 = {1, 2, 3}
set2 = {"f", "e", "d", "c", "b", "a"}

equality_check = set1 == set2
difference_check = set1.isdisjoint(set2)
print("Sind set1 und set2 gleich?", equality_check)
print("Enthalten set1 und set2 unterschiedliche Elemente?", difference_check)