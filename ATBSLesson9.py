#functions --> grouping code that would be executed multiple times 

def hello():
    print("Hello")
    print('Howdy')
    print('Howdy there')
hello()


#adding arguments 
def hello1(name):
    print("Hello "+name)
hello1('Kenny')

def plusOne(number):
    return number+1
newnum=plusOne(6)
print(newnum)