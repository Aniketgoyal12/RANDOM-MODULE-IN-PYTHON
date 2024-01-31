#Program of Rock Paper Scissor

import random

user_input = input("Enter your choice (R/P/S)")

comp_choice = random.randint(0,2)
#print(comp_choice)

if comp_choice == 0 and (user_input == 's' or user_input == 'S'):
    print("Computer Wins")
elif comp_choice == 1 and (user_input == 'r' or user_input == 'R'):
    print("Computer Wins")
elif  comp_choice == 2 and (user_input == 'p' or user_input == 'P'):
    print("Computer Wins")
else:
    print("User Wins")
