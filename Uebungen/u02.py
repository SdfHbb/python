# 1️⃣
secret_number = 7

# 2️⃣
guess_number = int(input("2️⃣ Erraten Sie die Zahl (1-10)⬅️ "))

# 3️⃣
if guess_number == secret_number:
  input("3️⃣ Treffer!")
  # 4️⃣
elif guess_number > secret_number:
  input(f"4️⃣ Ihre Zahl ist zu groß")
else:
  input(f"4️⃣ Ihre Zahl ist zu klein")
