import random
import random

lottozahlen = sorted(random.sample(range(1, 50), 6))
print(lottozahlen)

########## v2 ###############

# lottozahlen = []
# while len(lottozahlen)<6:
#     zufallszahl = random.randint(1, 49)
#     if zufallszahl not in lottozahlen:
#         lottozahlen.append(zufallszahl)
#
# lottozahlen.sort()
# print(lottozahlen)


########## v4 ###############

# lottozahlen = []
# for i in range(1, 49 + 1):
#   lottozahlen.append(i)
#
# random.shuffle(lottozahlen)
# result = []
# for i in range(0, 6):
#   result.append(lottozahlen[i])
# print(sorted(result))

########## v4 ###############

lotto = []

# def play_game():
#     richtig = 0
#     for i in range(6):
#         if int(input("Bitte Zahl tippen: ")) in lotto:
#             richtig += 1
#     print(f"Du hast {richtig} richtige getippt")
#
#
# def lotto_gen():
#     while len(lotto) < 6:
#         zahl = random.randint(1, 49)
#         if zahl not in lotto:
#             lotto.append(zahl)
#     print(sorted(lotto))
#     play_game()
#
#
# lotto_gen()
