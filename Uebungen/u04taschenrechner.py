while True:
  try:
    zahl1 = int(input("Bitte Zahl1: "))
    break
  except:
    print("Zahl erforderlich!")

while True:
  try:
    operator = input("Wähle Operator: ")
    if operator == "+" or operator == "-" or operator == "*" or operator == "/":
      break
    else:
      print("Gültige Operatoren (+ - / *): ")
  except:
    print()

while True:
  try:
    zahl2 = int(input("Bitte Zahl2: "))
    break
  except:
    print("Zahl erforderlich!")


