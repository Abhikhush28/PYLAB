sentances = "fp39968hft3fjp5v2bhfh0luc8visgjwzlksft7u35hez2qnbtp6bg5euc9ffhiugmgpayadfcwfv0l0qwhf2se7xxzbtxfwy79mq6uvxkbclfesrpplfau8lkoi4n6c"

def is_int(x):
 if x in "0123456789":
  return True
 else:
  return False


strings = list(filter(lambda x: x.isdigit() == False , sentances))
number = list(filter(lambda x: x.isdigit() == True , sentances))
number = list(map(lambda x : int(x), number))
print("String: ", strings)
print("\nInterger: ", number)