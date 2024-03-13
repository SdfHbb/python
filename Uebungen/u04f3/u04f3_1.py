def umfang(**kwargs):
  if "breite" in kwargs and "hoehe" in kwargs:
    return print(f"""Breite {kwargs["breite"]}  
Hoehe {kwargs["hoehe"]} 
➡️ Umfang {2 * (kwargs["breite"] + kwargs["hoehe"])} 
""")
  else:
    return None

umfang(breite= 4, hoehe=5)