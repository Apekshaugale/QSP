#11.Check whether the length of the given word is odd.
#using if else condition
b=str(input('Enter the word :'))
if len(b)%2==0:
    print(f'The length of the given word {b} is even.')
else:
    print(f'The length of the given word {b} is odd.')

 #using !=   
b=str(input('Enter the word :'))
if len(b)%2!=0:
    print(f'The length of the given word {b} is odd.')

#using &
b=str(input('Enter the word :'))
if (len(b)&1)==1:
    print(f'The length of the given word  {b} is odd')


 #using %   
b=str(input('Enter the word :'))
if len(b)%2==1:
    print(f'The length of the given word {b} is odd')
    
