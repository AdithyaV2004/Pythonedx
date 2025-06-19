#Converts inputted items into an ordered list

li={}
def main():
    while True:
        try:
            it=input()
            if it.upper() not in li:
                li[it.upper()]=1
            else:
                li[it.upper()]+=1
        except EOFError:
            disp()
            return

def disp():
    for i in sorted(li.keys()):  #List is sorted alphabetically
        print(f"{li[i]} {i}")

main()

