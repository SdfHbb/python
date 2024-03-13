def checkAnagramm(str1, str2):
  str1 = str1.lower()
  str2 = str2.lower()
  return sorted(str1) == sorted(str2)

print(checkAnagramm("Listen","silent"))