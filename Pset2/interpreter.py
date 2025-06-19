#Calculator Oversimplified


def main():
  exp=input("Expression: ")
  x, y, z = exp.strip().split(" ")    # Split on basis of space between them
  calc(float(x), y, float(z))    # Call function

def calc(x,y,z):
  match y:        # Check for the operation
    case "+":
      print(x + z)
    case "-":
      print(x - z)
    case "*":
      print(x * z)
    case "/":
      print(x / z)

main()
