def dict_mit_max_value(myDict):
  return max(myDict, key=myDict.get)


myDict = {'a': 1, 'b': 3000, 'c': 0}

print(dict_mit_max_value(myDict))