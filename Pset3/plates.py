#Teaches how to put vehicle plates

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not s[0:2].isalpha():      #tTo check if first two chars are alpha
      return False
    if not 2<=len(s)<=6:             #To check length of s
        return False
    if s.count(".")>0 or s.count(" ")>0 or s.count(",")>0:    #To check for special chars
      return False
    if f_no(s):     #Call function to check first number
       return False
    return True

def f_no(s):     #To check if first number is 0
  ind=len(s)     # To avoid error in case of full alpha
  for i in s:
    if i.isdigit():
      ind=s.index(i)
      if i=="0":
        return True
      break
  for i in range(ind,len(s)):     #To check whether alpha comes after number
    if s[i].isalpha():
      return True

main()
