set1 = {"a", "b", "c"}
set2 = {"f", "e", "d", "c", "b", "a"}

print(f"set1 Teilmenge von set2? ➡️ {set1.issubset(set2)}")

set1 = set1.clear()
print(f"Lösche alle Elemente aus set1 ➡️ {set1}")

del set2

try:
  print(set2)
except:
  print("set2 wurde gelöscht")