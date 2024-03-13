def selbstaufruf():
  try:
    # 1️⃣
    zahl = int(input(f"1️⃣ Bitte Zahl eingeben⬅️ "))
    # 2️⃣
    while zahl > 0:
      # 4️⃣
      if zahl == 0:
        break
      # 3️⃣
      else:
        print(f"2️⃣ Python rockt!")
        zahl -= 1
        # 5️⃣
        print(f"5️⃣ while-Schleife durchlaufen")
  # 6️⃣
  except:
    print("6️⃣ Eingabe muss eine Zahl sein! ⬅️")
    selbstaufruf()

selbstaufruf()