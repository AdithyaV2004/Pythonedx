import random


def main():
    l=get_level()
    score=simulate_game(l)
    print("Score:",score)

def get_level():
    while True:
        try:
            l=int(input("Level: "))
            if l not in [1,2,3]:
                raise Exception
            return l
        except:
            pass

def generate_integer(level):
    if level==1:
        n=random.randint(0,9)
    else:
        n=random.randint(10**(level-1),10**(level)-1)
    return n

def simulate_round(x,y):
    count_tries=1
    while count_tries<=3:
        try:
            answer=int(input(f"{x} + {y} = "))
            if answer==(x+y):
                return True
            else:
                print("EEE")
                count_tries+=1
        except:
            count_tries+=1
            print("EEE")
    print(f"{x} + {y} = {x+y}")
    return False

def simulate_game(level):
    count_round=1
    score=0
    while count_round<=10:
        x,y=generate_integer(level),generate_integer(level)
        response=simulate_round(x,y)
        if (response):
            score+=1
        count_round+=1
    return score

if __name__ == "__main__":
    main()
