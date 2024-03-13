def palindrome(str):
  str = str.casefold()
  str2 = str[::-1]
  if str2 == str:
    return print(f"[{str}] ist ein Palindrom")
  else:
    return print(f"[{str}] ist kein Palindrom")

palindrome("Hello")
palindrome("Anna")