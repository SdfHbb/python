mixed_set = {1, "Hello", 3.14, True, 42, "World", False}
numbers_set = {x for x in mixed_set if isinstance(x,
(int, float))}
print("Nur die Zahlen aus mixed_set:", numbers_set)