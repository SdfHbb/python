def laenge(str1, str2):
  if len(str1) > len(str2):
    return print(f"String1 is länger als String2")
  elif  len(str1) < len(str2):
    return print(f"String1 is kürzer als String2")
  else:
    return print(f"String1 und String2 sind gleich lang")

laenge("Hello", "World!")

