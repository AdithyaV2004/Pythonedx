from random import randint

while True:
    try:
        level=int(input("Level: "))
        if level>0:
            break
    except Exception as e:
        pass

rand_num=randint(1,level)

while True:
    try:
        guess=int(input("Guess: "))
        if guess>0:
            if guess<rand_num:
                print("Too small!")
            elif guess>rand_num:
                print("Too large!")
            else:
                print("Just right!")
                break
    except Exception as e:
        pass
