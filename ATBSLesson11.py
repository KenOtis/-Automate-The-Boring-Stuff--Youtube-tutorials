#detecing errors and still running 
#try and except statements 
def divide42by(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError: #You do not have to specify the error 
        print("Error: You tried to divide by 0.")

print(divide42by(3))
print(divide42by(12))
print(divide42by(0)) #You get an error on this one and the whole program crashes
print(divide42by(1))

#How many cats do you have: six--> not 6 
print('How many cats do you have?')
numCats=input()
try:
    if int (numCats)>=4: 
        print("That is alot of cats. ")
    else:
        print("That is not many cats.")
except ValueError:
    print("You did not enter a number.")