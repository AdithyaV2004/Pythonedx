#Discrimination based on greeting

def main():
  greeting=input("Enter greeting:")
  price=value(greeting)
  print(f"${price}")

def value(greetings):
  greetings = greetings.lower().strip()
  if "hello" in greetings:
    return 0
  elif greetings[0] == "h":
    return 20
  else:
    return 100

if __name__ == "__main__":
  main()
