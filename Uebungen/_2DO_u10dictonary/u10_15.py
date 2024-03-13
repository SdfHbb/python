def commonKeys(dict1, dict2):
  list = []
  for key in dict1.keys() and dict2.keys():
    list = list.append(key)
  return list


x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = commonKeys(x, y)
print(z)
