#Prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

user = input("Enter the input: ")    # Ask user for input
user = user.replace(" ","...")       # Replace space with dots
print(user)                          # Print output
