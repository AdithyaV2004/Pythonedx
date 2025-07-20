#Replace your fuel gauge with ts(Dont do it you ret**d)

def main():
    try:
        f=input("Fraction: ")  #Takes a fraction as input and converts to percentage
        l=f.split("/")
        num=int(l[0])
        den=int(l[1])
        fuel=convert(num,den)
        print(fuel)
        return
    except:
        None


def convert(s):
    l=s.split("/")
    n=int(l[0])
    d=int(l[1])
    if d==0:
        raise ZeroDivisionError
    if n>d or type(n)==type(d)!=int:
        raise ValueError
    fuel=n/d*100
    fuel_int=round(fuel,0)
    new_fuel=gauge(int(fuel_int))
    return int(new_fuel[0:-1])

def gauge(percentage):
    if percentage<=1:
        return "E"
    elif percentage>=99:
        return "F"
    else:
        return f"{percentage}%"


main()
