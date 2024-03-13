def filter_dict(myDict, limit):
  z = {}
  for key, value in myDict.items():
    if value > limit:
      z[key] = value
  return z


x = {'a': 1, 'b': 2, 'c': 4, 'd': 5}
z = filter_dict(x, 3)
print(z)
