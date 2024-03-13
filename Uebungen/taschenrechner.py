def taschenrechner(operand1, operand2, rechenart):
  if rechenart == "+":
    return operand1 + operand2
  elif rechenart == "-":
    return operand1 - operand2
  elif rechenart == "*":
    return operand1 * operand2
  elif rechenart == "/":
    if operand2 == 0: print("Division durch 0 ist nicht erlaubt.")
    else:
      return operand1 / operand2
  else:
    return "Ungültiger Parameter."

zahl1 = int(input("Zahl Nummer 1: "))
zahl2 = int(input("Zahl Nummer 2: "))
rechenart = input("Rechenart: '+' '-' '*' '/' > ")
result = taschenrechner(zahl1, zahl2, rechenart)
print(f"{zahl1} {rechenart} {zahl2} ist gleich: {result}")


################### P ################



# while True:
#   try:
#     zahl1 = int(input("Zahl1: "))
#     break
#   except:
#     print("Eingabe für Zahl1 muss eine Zahl sein: ")
#
# while True:
#   try:
#     operator = input("Operator: ")
#     if (operator == "+" or operator == "-" or operator == "*" or operator == "/"):
#       break
#     else:
#       print("Operator muss (+  -  *  /) sein: ")
#   except:
#     print()
#
# while True:
#   try:
#     zahl2 = int(input("Zahl2: "))
#     if (operator == "/" and zahl2 != 0):
#       break
#     else:
#       print("Zahl2 darf nicht 0 sein: ")
#   except:
#     print("Eingabe für Zahl2 muss eine Zahl sein: ")
#
#
# def addiere(zahl1, zahl2):
#   return zahl1 + zahl2
#
#
# def subtrahiere(zahl1, zahl2):
#   return zahl1 - zahl2
#
#
# def multipliziere(zahl1, zahl2):
#   return zahl1 * zahl2
#
#
# def dividiere(zahl1, zahl2):
#   return zahl1 / zahl2
#
#
# if (operator == "+"):
#   print(addiere(zahl1, zahl2))
# elif (operator == "-"):
#   print(subtrahiere(zahl1, zahl2))
# elif (operator == "*"):
#   print(multipliziere(zahl1, zahl2))
# elif (operator == "/"):
#   print(dividiere(zahl1, zahl2))
