def merge_dicts(x, y):
  z = x.copy()  # start with keys and values of x
  for key, value in y.items():
    if key in z:
      z[key] +=value
    else:
      z[key] =value
  return z


x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = merge_dicts(x, y)
print(z)