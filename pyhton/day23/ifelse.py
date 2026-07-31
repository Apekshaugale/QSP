'''
1.WAP to check length of both string collections are equal or not. if both are equal
print the concat the two strings and display, or else if any one of the collection
not equal print both the collections with lengths
'''
'''
string1=eval(input('Enter the string 1:'))
string2=eval(input('Enter the string 2:'))
if string1==string2:
    print(string1+string2)
else:
    print(f'{string1} has lenght',len(string1))
    print(f'{string2} has lenght',len(string2))
'''
'''
2.WAP to check whether both given values point to the same memory location or
not. if it is true print the middle item of the second collection, or else if it is false
print the first item and last item of the first collection along with the memory
address.'''
'''
value1=eval(input('Enter the value1:'))
value2=eval(input('Enter the value2:'))
if  id(value1)==id(value2):
    mid=(len(value2)-1)//2
    print(value1[mid])
else:
    print(f' The first item  {value1[0]}   and  memory address is {id(value1[0])}')
    print(f' last item   {value1[-1]}  and memory address is {id(value1[-1])}  ' )


'''
'''
v1=eval(input('Enter the value1:'))
v2=eval(input('Enter the value2:'))
if id(v1)==id(v2):
    mid=(len(v2)-1)//2
    print(v2[mid])
else:
    print(f' The first item  {value1[0]}   and  memory address is {id(value1[0])}')
    print(f' last item   {value1[-1]}  and memory address is {id(value1[-1])}  ' )

'''


'''
3.WAP to check whether a given string collection is more than ten, and the first +
last character of the ascii values should be divisible by 5, if condition is satisfied
print first, middle, last characters ASCII values or else print the string three
times.
'''
'''
s=eval(input('Enter the string:'))   

if  len(s)>10 and (ord(s[0])+ord(s[-1]))%5==0:
    print('first character : ',ord(s[0]))
    print('middle character :',ord(s[(len(s)-1)//2]))
    print('last character :',ord(s[-1]))
else:
    print(s*3)

OR

s=eval(input('Enter the string:'))    
a=(s[0])
print(a)
b=(s[-1])
print(b) 
if  len(s)>10 and ord(a)+ord(b)%5:
    print('first character : ',ord(s[0]))
    mid=(len(s)-1)//2
    print('middle character :',ord(s[mid]))
    print('last character :',ord(s[-1]))
else:
    print(s*3)

'''

'''4.WAP to check whether the middle of the item present in the list is string data type
or not if it is string print that list or else if it is not string then print that middle
item.'''
'''
L=eval(input('Enter the list:'))
mid=(len(L)-1)//2          #position of mid 
if type(L[mid])==str:      #for value -->vn[mid]
    print(L)
else:
    print(L[mid])
    
    '''
'''5.WAP Given a string, return a new string where the first and last characters have
been exchanged.'''


'''6.Write a program to find out such numbers which are divisible by 7 but are not a
multiple of 5. Both the conditional is satisfied and print actual value. if one
condition is not satisfied actual number is multiply by 4 and print result.'''

'''num=eval(input('Enter the number: '))
if  num%7==0 and num%5!=0:
    print('Actual value is  :',num)
else:
    print(num*4)
'''

'''7.WAP to check whether two values are pointing to the same memory address or
not. If the same memory displays the address or else displays the two values
addresses.'''
'''
v1=eval(input('Enter the value1:'))
v2=eval(input('Enter the value2:'))
if id(v1)==id(v2):
    print(id(v1))
else:
    print('memory address of value 1',id(v1))
    print('memory address of value 2',id(v1))
'''

'''8.WAP to check whether a given input character is a special symbol or not if it is a
special symbol then print that character three times and tell print that character
5 times.'''
'''
char=eval(input('Enter the character:'))
if not char.isalnum():
    print(char*3)
else:
    print(char*5)
   '''


'''9.WAP to check length of both string collections equal or not if it is equal print the
connection of any one of the collections if it is not equal print both the collection.'''
'''string1=eval(input('Enter the string 1:'))
string2=eval(input('Enter the string 2:'))
if len(string1)==len(string2):
    print(string1+string2)
else:
    print(' string 1  : 'string1)
    print(' string 2 : 'string2)
'''


'''10.WAP To check whether both input variables point to the same memory location
or not if it is true print the last item of the second collection, if it is false print the
first item of the first collection along with the memory address.'''
'''s1=eval(input('Enter the variable1:'))
s2=eval(input('Enter the variable 2:'))
if id(s1)==id(s2):
    print(f'The last item of the second collection is "{s2[-1]}".')
else:
    print(f'first item of the first collection is {s1[0]} and memory address is  {id(s1[0])}')
'''


'''11.WAP to print the string collection five times when the length of the string
collection should be more than 3 and the middle character of the string should
be vowel and the first character ASCII value should be even, to print the previous
character of middle character, or else if ASCII value is odd then print the string
three times as print that string.'''
string=eval(input('Enter the string :'))
mid=(len(string)-1)//2
#if len(string)>3 and string[mid] in 'aeiouAEIUO'  and chr(ord(string[0]))%2==0
if len(string)>3 and string[mid] in 'aeiouAEIUO' :
    if ord(string[0])%2==0 :
        print(chr(ord(string[mid])-1))
        print(string*5)
else:
    print(string*3)
