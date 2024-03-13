set1 = {1, 2, 3}
set2 = {"f", "e", "d", "c", "b", "a"}
set3 = {13, 14, 15}

set3.update(set2).difference_update(set1)
print("set3 nach den Operationen:", set3)