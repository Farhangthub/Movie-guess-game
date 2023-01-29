import random

movies =[" The Dark Knight", "Angry Men","Pulp Fiction","The Matrix"] 
com_choice=random.choice(movies)
guess_count=0
my_earn_point=0
com_earn_point=0
my_choice=""
while guess_count != 10:
    my_choice=input("Enter your guess:")
    if my_choice == com_choice :
        my_earn_point +=1
        guess_count +=1
    else:
        com_earn_point +=1
        guess_count +=1
    

print("The Game is over")
if my_earn_point > com_earn_point :
    print("I have won the game!")
else:
    print("Computer has won the game!")



