#Outputs meal appropriate to time

def main():
    time = input("What's the time? ")
    time = convert(time)   # Calls convert function

    if 7 <= time <=8:        # Check for breakfast time
      print("breakfast time")
    elif 12 <= time <= 13:       # Check for lunch time
      print("lunch time")
    elif 18 <= time <= 19:      # Check for dinner  time
      print("dinner time")

      # Output nothing for other cases

def convert(time):
    hour, minute = time.split(":")         # Split at ":" and store in two seperate variables
    n_time = float(hour) + (float(minute)/60)       # Do calculations
    return(n_time)

if __name__ == "__main__":     # Direct Call? I guess?? Don't know yet.
    main()
