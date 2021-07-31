#While loops 
spam=0 
while spam<5:
    print("Hello world")
    spam=spam+1

name=' '
while name != 'your name':
    print('Please type your name: ')
    name=input()
print('Thank you')


#infinite loops 
#while True:
#    print("Hello World! ")

spam=0 
while spam<5:
    spam=spam+1
    if spam==3:
        continue ##This will not print the following statement  when ==3
    print('Spam is: ' + str (spam))