def main():
    l=[]
    try:
        while True:
            str=input("Name: ")
            l.append(str)
    except EOFError:
        if len(l)==1:
            print(f"\nAdieu, adieu, to {l[0]}")
        elif len(l)==2:
            print(f"\nAdieu, adieu, to {l[0]} and {l[1]}")
        else:
            print("\nAdieu, adieu, to ",end="")
            for i in l[:-1]:
                print(i, end=", ")
            print(f"and {l[-1]}")

main()

