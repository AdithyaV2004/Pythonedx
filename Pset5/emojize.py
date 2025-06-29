from emoji import emojize
def main():
    str=input()
    print(emojize(f":{str}:",language='alias'))

main()
