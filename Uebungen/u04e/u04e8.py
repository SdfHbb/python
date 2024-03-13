def ersetzeString(hauptStr, suchStr, ersetzung):
  # print(hauptStr)
  if suchStr in hauptStr:
    hauptStr = hauptStr.replace(suchStr, ersetzung)
    return print(hauptStr)
  else:
    print("Suchstring nicht vorhanden")

ersetzeString("Hellö Wörld!", "ö Wö", "o Wo")