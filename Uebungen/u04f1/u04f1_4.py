def berechne_mehrwertsteuer(netto, mwst_satz):
  return netto * mwst_satz / 100


def gesamt_bruttobetrag(netto, mwst_satz):
  return print(f"""
Netto  {netto:.2f}€
MwSt    {berechne_mehrwertsteuer(netto, mwst_satz):.2f}€
Brutto {berechne_mehrwertsteuer(netto, mwst_satz) + netto:.2f}€
""")


gesamt_bruttobetrag(100, 19)
