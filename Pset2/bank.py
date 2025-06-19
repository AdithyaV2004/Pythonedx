#Discrimination on based on greeting

greetings = input("Greetings: ")
greetings = greetings.lower().strip()
if "hello" in greetings:    #Corresponds to basketball people
  print("$0")
elif greetings[0] == "h":
  print("$20")
else:
  print("$100")
