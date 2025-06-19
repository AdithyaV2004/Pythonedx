#What is the answer to the Great Question of Life, the Universe and Everything

l=["42","forty-two","forty two"]     #list of all possible answers
ans=input("What is The Answer to the Great Question Of Life, the Universe and Everything? " )
ans=ans.lower()    #convert cases
ans=ans.strip()    #Strip spaces
if ans in l:       
  print("Yes")
else:
  print("No")
