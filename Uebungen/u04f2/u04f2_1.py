def summe(*args):
  text = ""
  for i in args:
    text += str(i) + " "
  return print(f"Summe von {text} ➡️ {sum(args)}")

summe(1,2,3,4)
summe(1,2,3,4,5,6,7,8,9,10)