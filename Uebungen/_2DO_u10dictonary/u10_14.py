def reverse_dict(myDict):
  z = {}
  for key, value in myDict.items():
    z[value] = key
  return z

x = {'a': 1, 'b': 2, 'c': 4, 'd': 5}
z = reverse_dict(x)
print(z)
