#Replace fake emojis with real emojis


def convert(str):
    return str.replace(":)","🙂").replace(":(","🙁")   #Does necessary conversions

def main():
    str=input()
    n_str=convert(str)     #Calls function with argument
    print(n_str)

main()   #Calls function
