import random

"""
Rock - Paper - Scissors

Ein kleines Spiel (Schere, Stein, Papier) um Ihnen ein bisschen Python zu
zeigen.
"""

#  Variablen anlegen
ROCK = "r"
PAPER = "p"
SCISSORS = "s"

TIE = "Tie."
WIN = "You win :-)"
LOSE = "You lose :-("


# Eine Funktion mit Parametern
def compare_moves(you, computer):
  # Wenn--Dann-Vergleiche
  if you == computer:
    return TIE
  elif you == SCISSORS and computer == PAPER:
    return WIN
  elif you == ROCK and computer == SCISSORS:
    return WIN
  elif you == PAPER and computer == ROCK:
    return WIN
  else:
    # ... in allen anderen Fällen
    return LOSE


you = ""

# While-Schleife
while you not in [ROCK, PAPER, SCISSORS]:
  # Eingabe
  you = input("(r)ock, (p)aper, or (s)cissors? > ")

# Funktionsaufrufe
computer = random.choice([ROCK, PAPER, SCISSORS])
result = compare_moves(you, computer)

########### P ####################

# while True:
#   try:
#     eingabe = input("Bitte wählen (r)ock (p)aper oder (s)cissor: ")
#     myList = ["r", "p", "s"]
#     pc = random.choice(myList)
#     print(pc)
#
#     if (eingabe == "r" and pc == "s"):
#       print("Stein schlägt Schere")
#
#     elif (eingabe == "r" and pc == "p"):
#       print("Papier schlägt Stein")
#
#     elif (eingabe == "s" and pc == "p"):
#       print("Schere schlägt Papier")
#
#     elif (eingabe == "s" and pc == "r"):
#       print("Stein schlägt Schere")
#
#     elif (eingabe == "p" and pc == "s"):
#       print("Schere schlägt Papier")
#
#     elif (eingabe == "p" and pc == "r"):
#       print("Papier schlägt Stein")
#     else:
#       print("Unentschieden")
#
#     eingabe = input("weiterspielen? j | n")
#     if (eingabe == "n"):
#       break
#
#   except:
#     print()
