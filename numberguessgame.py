#import random module to let the computer chose the number

import random

#using randint function let the computer choose the number

comp_choice = random.randint(0,100)


#take the user input of the number
#specify the number of chances using for loop

for i in range(1,6):
    user_in = int(input("Enter your number between 1 to 100"))
    
    if  user_in < comp_choice and comp_choice - user_in > 10:
        print(f"TOO SMALL. TRY AGAIN! YOU HAVE {5-i} chances left")
    elif user_in > comp_choice and user_in - comp_choice > 10 :
        print(f"TOO LARGE. TRY AGAIN! YOU HAVE {5-i} chances left")
    elif user_in == comp_choice:
        print("CONGRATS, YOU WON!")
        break
    else:
        print("SORRY:( YOU HAVE EXHAUSTED YOUR ATTEMPTS")
    
