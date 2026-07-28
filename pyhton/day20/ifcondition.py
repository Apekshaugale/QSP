'''
#1.Write a program to check whether the given number is divisible by 5.
num=eval(input('Enter the number :'))
if num%5==0:
    print(f'The number {num} is divisible by 5')
'''

'''
#2.Write a program to check whether the given number is divisible by 10.
num=eval(input('Enter the number :'))
if num%5==0:
    print(f'The number {num} is divisible by 5')

#3.Write a program to check whether the given number is greater than 100.
num=eval(input('Enter the number :'))
if num>100:
    print(f'The number {num} is greater than 100.')    

#4.Write a program to check whether the given number is less than 50.
num=eval(input('Enter the number :'))
if num<50:
    print(f'The number {num} is less than 50.')    

#5.Write a program to check whether the given character is uppercase.
string=eval(input('Enter the character : '))
if string.isupper():
    print(f'the given character {string} is uppercase.')
   
#6.Write a program to check whether the given character is lowercase.
string=eval(input("Enter the character :"))
a=string
if a.islower():
    print(f'the given character {string} is lowercase.')

string=eval(input("Enter the character :"))
a=string
if a.islower():
    print(f'the given character {a} is lowercase.')

#7.Write a program to check whether the given string starts with "P".
a=eval(input("Enter the character :"))
if a.startswith('P'):
    print(f'the given string {a} starts with "P".')

#8.Write a program to check whether the given string ends with "n".
b=eval(input("Enter the character :"))
if b.endswith('n'):
    print(f'the given string {b} ends with "n".')


#9.Write a program to check whether the given string contains only alphabets.    
b=eval(input("Enter the character :"))
if b.isalpha():
    print(f'The given string {b} contains only alphabets.')
else:
    print(f'The given string {b}  does not contains only alphabets.')
    
#10.Write a program to check whether the given string contains only digits.
b=str(input("Enter the string :"))
if b.isdigit():
    print(f'The given string {b} contains only digit .')
else:
    print(f'The given string {b}  does not contains only digit.')

b=eval(input("Enter the string :"))
if b.isdigit():
    print(f'The given string {b} contains only digit .')
else:
    print(f'The given string {b}  does not contains only digit.')

string=eval(input("Enter the string :"))
a=string
if a.isdigit():
    print(f'The given string {a} contains only digit .')
else:
    print(f'The given string {a}  does not contains only digit.')



#11.Check whether the length of the given word is odd.
b=str(input('Enter the word :'))
if len(b)%2==0:
    print(f'The length of the given word {b} is even.')
else:
    print(f'The length of the given word {b} is odd.')

    
b=str(input('Enter the word :'))
if len(b)%2!=0:
    print(f'The length of the given word {b} is odd.')


b=str(input('Enter the word :'))
if (len(b)&1)==1:
    print(f'The length of the given word {b} is odd')


    
b=str(input('Enter the word :'))
if len(b)%2==1:
    print(f'The length of the given word {b} is odd')
    

''''''
#12.If the given number is odd, convert it into float.
a=eval(input('Enter the number:'))
if a%2==1:
    print(f'The given number {a} is odd.')
    b=float(a)
    print(b)


#13.If the given number is even, convert it into string.
a=eval(input('Enter the number :'))
if a%2==0:
    print(f'The given number {a} is even.')
    b=str(a)
    print(b)


#14.If the given number is odd, store it in a list.
a=eval(input('Enter the number:'))
if a%2==1:
    print(f'The given number {a} is odd.')
    b=[]
    b.append(a)
    print(b)

#15Store an even number into a list without using append()
a=eval(input('Enter the number:'))
if a%2==0:
    print(f'The given number {a} is even.')
    b=[a]
    print(b)

#16If the given string length is even, convert it into uppercase.
a=str(input('Enter the string :'))
if (len(a)%2)==0:
    print(f'The length of string {a} is even.')
    print(a.upper())


a=str(input('Enter the string :'))
if (len(a)&1)==0:
    print(f'The length of string {a} is even.')
    print(a.upper())


a=str(input('Enter the string :'))
if len(a)%2!=1:
    print(f'The length of string {a} is even.')
    print(a.upper())

#17.If the given string length is odd, convert it into lowercase.
a=str(input('Enter the string :'))
if (len(a)%2)==1:
    print(f'The length of string {a} is odd.')
    print(f'The lowercase output of {a} is ',a.lower())


a=str(input('Enter the string :'))
if (len(a)&1)==1:
    print(f'The length of string {a} is odd.')
    print(f'The lowercase output of {a} is ',a.lower())


a=str(input('Enter the string :'))
if len(a)%2!=0:
    print(f'The length of string {a} is odd.')
    print(f'The lowercase output of {a} is ',a.lower())

#18.If the given word starts with "A", print its length.
a=str(input('Enter the word :'))
if a.startswith("A"):
    print(f'The length of "{a}" is ',len(a))


  
#19.If the given word ends with "e", convert it into title case.

a=str(input('Enter the word :'))
if a.endswith('e'):
    print(f'The given word "{a}" is ends with "e".')
    print(a.title())
    
#20.If the given string is alphabetic, print its first character.
string=str(input('Enter the string : '))
if string.isalpha():
    print(f'The first character of "{string}" is ',string[0])
   
#21.Check whether the number is even without using % and //
num=eval(input('Enter the number :'))
if (num &1)==0:
    print(f'The number "{num}" is even.')


#22.Check whether the number is odd without using %.
num=int(input('Enter the number :'))
if num&1==1:
    print(f'The number "{num}" is odd')

if (num//2)*2!=1:
    print(f'The number "{num}" is odd')
'''

#23.Check whether the length of the string is even using only len().
