#Converts camelCase to snake_case

def main():
  cc=input("camelCase: ")
  sc=snake(cc)
  print(f"snake_case: {sc}")

def snake(st):
  l=""
  for s in st:
    if s.isupper():
      l=l+"_"+s.lower()
    else:
      l+=s
  return l

main()
