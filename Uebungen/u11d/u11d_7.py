prime_set = set(())

prime_set = {2, 3, 5, 7}
composite_set = {4, 6, 8, 9, 10}
union_primes_composites = prime_set.union(composite_set)
intersection_primes_composites = prime_set.intersection(composite_set)
difference_primes_composites = prime_set.difference(composite_set)
print("Vereinigung von prime_set und composite_set:",union_primes_composites)
print("Schnittmenge von prime_set und composite_set:",intersection_primes_composites)
print("Differenz von prime_set und composite_set:", difference_primes_composites)