def delVocale(str):
  vocale = "aeiouAEIOU"
  result = "".join(char for char in str if char not in vocale)
  return print(result)

delVocale("Hello WOrldiaeiou")