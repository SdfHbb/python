def countChar(str):
  print(str)
  str = str.lower()
  return print(f"Häufigstes Zeichen ➡️ {max(set(str), key=str.count)}")

countChar("Programmierung ist eine großartige Fähigkeit.")