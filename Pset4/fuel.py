#Replace your fuel gauge with ts(Dont do it you ret**d)

def main():
    while True:
        try:
            f=input("Fraction: ")  #Takes a fraction as input and converts to percentage
            l=f.split("/")
            num=int(l[0])
            den=int(l[1])
            percent(num,den)
            return
        except:
            None


def percent(n,d):
    if n>d or d==0:
        raise Exception
    fuel=n/d
    if fuel>=0.99:
        print("F")
    elif fuel<=0.01:
        print("E")
    else:
        p=fuel*100
        print(f"{int(round(p,0))}%")
    return

main()
