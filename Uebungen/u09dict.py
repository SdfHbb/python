# 1
myDict = {}

# 2
myDict["Name"] = "Max"
print(f"#2 {myDict}")

# 3
wert = myDict.get('Key', 'Nicht vorhanden')
print(f"#3 {wert}")

# 4
myDict["Name"] = "Anna"
print(f"#4 {myDict}")

# 5
if "Name" in myDict:
  del myDict["Name"]
print(f"#5 {myDict}")

# 6
notenDict = {"Fach": "Mathematik", "Note": 9}
print(f"#6 {notenDict}")

# 7
notenDict["Gewichtung"] = 2
print(f"#7 {notenDict}")

# 8
def durchschnittsnote(notenDict):
  summe = notenDict["Note"] * notenDict["Gewichtung"]
  gewichtung = notenDict["Gewichtung"]
  durchschnitt = summe / gewichtung
  return durchschnitt

# 9
ergebnis = durchschnittsnote(notenDict)
print("Der gewichtete Durchschnitt ist:", ergebnis)

# 10
studenten_liste = [
{"Name": "Max", "Alter": 20, "Note": 8},
{"Name": "Anna", "Alter": 22, "Note": 9},
{"Name": "Tom", "Alter": 21, "Note": 7}
]
print(f"#10 {studenten_liste}")
