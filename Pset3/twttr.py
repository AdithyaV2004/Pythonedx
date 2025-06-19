#Takes out the vowels to create abominations for names

def main():
  txt=input("Input: ")
  out=shorten(txt)
  print(out)

def shorten(s):
  l=""
  for i in s:
    if i.lower() not in ['a','e','i','o','u']:     #To filter out the vowels
      l+=i
  return l

if __name__ == "__main__":
  main()
