#Replace the waiter at taqueria with ts(Go ahead, its fireee)

menu={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    tot=0
    while True:
        try:     #Continues taking order till EOF 
            it=input("Item: ")
            tot=tot+menu[it.title()]
            print(f"Total: ${tot:.2f}")
        except EOFError:
            return
        except:
            None
main()





