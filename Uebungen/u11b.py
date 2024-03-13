set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = set((6, 7, 8, 9, 10))

# 1
union_set = set1.union(set2)
print(f"Vereinigung ➡️ {union_set}")

# 2
intersection_set = set1.intersection(set2)
print(f"Schnittmenge ➡️ {intersection_set}")

# 3
difference_set = set1.difference(set2)
print(f"Delta ➡️ {difference_set}")
