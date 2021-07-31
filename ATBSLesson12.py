#Number Guessing game
import random
print("Hello, what is your name?")
name=input()
secretnum=random.randint(1,20)
print("Well, "+ name + ', I am thinking of a number between 1 and 20')

count=0
#ask the play to guess 6 times 
for quessesTaken in range(1,7):
    print('Take a guess.')
    count=count+1
    guess=int(input())
    if guess<secretnum:
        print('Your guess is too low.')
    elif guess>secretnum:
        print("Your guess is too high. ")
    else:
        break #this is the correct guess 
if guess==secretnum:
    print("Good Job, "+name+"! you guessed the correct number in "+ str(count))
else:
    print("Nope. the number i was thinking of was "+ str(secretnum))