def bmi(**kwargs):
  if "gewicht" in kwargs and "groesse" in kwargs:
    return print(f"""
Gewicht {kwargs["gewicht"]}kg
Größe {kwargs["groesse"]}m
BMI {kwargs["gewicht"] / pow(kwargs["groesse"],2):.2f}
""")
  else:
    return None

bmi(gewicht=86, groesse=1.75)