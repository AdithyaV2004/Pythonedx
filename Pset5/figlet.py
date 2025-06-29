import pyfiglet
import sys

def main():
    if len(sys.argv)==1:
        str=getstr()
        ascii_banner = pyfiglet.figlet_format(str)
    elif len(sys.argv)==3:
        try:
            if sys.argv[1] in ["-f","--font"]:
                ascii_banner = pyfiglet.figlet_format("str",font=sys.argv[2])
                str=getstr()
                ascii_banner = pyfiglet.figlet_format(str,font=sys.argv[2])
            else:
                sys.exit(2)
        except Exception:
            sys.exit(2)
    else:
        sys.exit(2)
    print(ascii_banner)

def getstr():
    return(input("Enter the string: "))

main()
