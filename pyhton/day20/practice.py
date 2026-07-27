#wap to check the given number is +ve (by using user-input)
'''
num =eval(input('Enter the number :'))
if num>0:
    print(f"The given number {num } is positive")
#check the number is negative
num=eval(input('Enter the number:'))
if num<0:
    print(f'The number {num} is negative')

    '''
'''
#wap to check the given number is even(using %)
num=eval(input('enter the number :'))
if num%2==0:
   print(f'The number {num} is even')
   '''
'''
#using (//)floor division
num1=eval(input('enter the number :'))
if (num1//2)*2==num1:
    print(f'the number {num1}is even')


#using (&)operator (1,1-->1)

num=eval(input('Enter the value :'))
if (num&1)==0:
    print(f"The number {num } is even")
    
#using (&)operator (1,1-->1)

num=eval(input('Enter the value :'))
if (num&1)==1:
    print(f"The number {num } is odd")
''

##wap to check the given word is even length
a="Pyhton Programming"
if len(a)%2==0:
    print(f"The lenght of {a} is even ")
'''
#wap to check the given number is even then convert to complex.
num=eval(input('enter number:'))
if num%2==0:
    print(complex(num))
