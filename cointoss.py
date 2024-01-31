import random
coin_toss = input("Do you want to flip the coin(Y/N)?")
if coin_toss == 'y' or coin_toss == 'Y':
    a = random.randint(0,1)
    if a == 0:
        print("Tails")
    else:
        print("Heads")
else:
    print("Bye!")
