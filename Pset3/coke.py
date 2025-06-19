#Simulated vending machine

def main():
  s=0
  while s<50:
    print("Amount due:",(50-s))
    s+=valid(int(input("Insert Coin: ")))
  print(f"Change Owed: {s-50}")

def valid(s):
  if s not in [25, 10, 5]:   #Do not accept random coins
    return 0
  else:
    return s

main()
