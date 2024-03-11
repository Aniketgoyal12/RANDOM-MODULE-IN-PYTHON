import random
com = random.randint(1,101)
score = 5
#print(com)
while 1:
    user = int(input("Enter the Number "))
    if user == com :
        print("You Won with", score, "attempts.")
        break
    elif user > com:
        print("Too Large")
        score -= 1
        print("you left", score, "attempts")
        if score == 0:
            print("you lose")
            break
    else:
        print("Too Small")
        score -= 1
        print("you left", score, "attempts")
        if score == 0:
            print("you lose")
            break
