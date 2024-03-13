set1 = {1, 2, 3}
set2 = {"f", "e", "d", "c", "b", "a"}

set1.update(set2)
set1.difference_update(set2)
set1.symmetric_difference_update(set2)
print("set1 nach den Veränderungen:", set1)
