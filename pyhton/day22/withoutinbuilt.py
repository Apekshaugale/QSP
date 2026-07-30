'''#1.wap to check the given number is even or odd (take user input)
()
#
num=eval(input('Enter the number : '))
'''

'''
#wap to check the given number is upper without using inbuild function.
a='HELLO'
x='H'
if ord('A')<=ord(x)<=ord('Z'):
    print(' The string is uppercase.')


#wap to check the given number is digit without using inbuild function.

d='7'
if ord('0')<=ord(d)<=ord('9'):
    print("It's a digit.")

#
e='5'
if e.isdigit():
    print('It is a digit.')




#wap to check given cahracter ia upper convert to lower.
k='HELLO'
if k.isupper():
    k=k.lower()
    print(k)

'''
#
'''
d='good morning'
if d.islower():
    d=d.upper()
    print(d)

#if we want to convert any lowercase char to uppercase take +32 because difference between alphabets. 
#without using inbuilt fuction upper into lower and vicevarsa
#upper to lower ===+32
#lower to upper=== -32    
e='H'
if ord('A')<=ord(e)<=ord('Z'): #true
    print(chr(ord(e)+32))
 


d='a'
if ord('a')<=ord(d)<=ord('z'):
    print(chr(ord(d)-32))
    print(d)



'''

#palindrome


