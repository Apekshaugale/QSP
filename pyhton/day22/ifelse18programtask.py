'''#1.wap to check the given number is even or odd (take user input)
num=eval(input('Enter the number : '))
if num%2==0:
    print(f'The given number "{num}" is even.')
else:
    print(f'The given number "{num}" is odd.')



#2.wap to check whether the male and female are eligible for wedding (take user input)
male=eval(input('Enter the age of male : '))
female=eval(input('Enter the age of female : '))
if male>=21 and female>=18:
    print(f'The male of age {male} and female of age {female} are eligible for wedding .')
else:
   print(f'The male of age {male} and female of age {female} are  not eligible for wedding .')



#3.wap to return uppercase if the char is lower,else return same char (by taking user input)
char=eval(input('Enter the character : '))
if char.islower():
    print('character in uppercase=',char.upper())
else:
    print('char')



#4.wap to return lower case if the upper ,else return same char (by taking user input)
char=eval(input('Enter the character : '))
if char.isupper():
    print('character in lowercase=',char.lower())
else:
    print('char')

    
#5.wap to find greater value among the two number
#n1=34
#n2=54

num1=eval(input('Enter the number 1 : '))
num2=eval(input('Enter the number 2 : '))
if num1>num2:
    print(f'The "{num1}" is greater than "{num2}" .')
else:
    print(f'The "{num2}" is greater than "{num1}" .')


    

#6.wap to check if the given number is even or not,if it is not even add+1 and make it even (take user input)
num=eval(input('Enter the number : '))
if num%2!=0:
    print(f'The number "{num}" is odd and its converted into  even is ',num+1)
else:
    print('The number is even .')

    
#7.wap to check whether the first character in the given string is starting with uppercase
#or Not if it is not Then capitalize it s="python".
char=eval(input('Enter the character : '))
if char[0]==char.isupper():
    print('The given string first character is in uppercase.')
else:
    print(char.capitalize())

    
#8.wap to check if the given number is even ,if it is even reduce it to its Half else make exponent (take user input)
num=eval(input('Enter the number : '))
if num%2==0:
    print(f'The given number "{num}" is even and its half is ',num/2)
else:
    print(f'The given number "{num}" is not even and its exponent is ',num**2)

#10.wap if the length of string is even then reverse else convert into upper case (take user input)
string=eval(input('Enter the string : '))
if len(string)%2==0:
    print('The length of string is even.',string[::-1])
else:
    print("The length of string is  not even and it is in uppercase =",string.upper())



#11.wap to check a number is +ve/-ve number (take user input)
num=eval(input('Enter the number : '))
if num>0:
    print('The number is positive.')
else:
    print('The number is negative.')


    
#12.wap to check a data is individual or collection data type or not (take user input)
data=eval(input('Enter the data : '))
if type(data) in (str,tuple,list,set,dict):
    print('The given data is collection data type.')
else:
    print('The given data is individual data type .')



#13.wap to check whether the specified character is present in the given string
c='A'
char=eval(input('Enter the String : '))
if c in char:
    print('The specified character is present in string.')
else:
    print('The specified character is not  present in string.')


#14.wap to check the length of dictionary is even or Not if even
#print as it is or else add a item and make it even

D={"a":"apple","b":"ball","c":"cat"}
if len(D)%2==0:
    print(D)
else:
    D.update({"d":"5"})
    print(D)


#15.wap to check the given number is greater than 5,if it is greater convert that number into negative number
#else print the same number
num=eval(input('Enter the number : '))
if num>5:
    print(-(num))
else:
    print(num)


#16.wap to check the given number is smaller than 10 ,if it is smaller find the exponent of it
#else print the number as it is
num=eval(input('Enter the number : '))
if num<10:
    print(f"The given number '{num}' is smaller than 10 and its exponent is ",num**2)
else:
    print(f"The given number '{num}' is greater than 10 then ",num)


#17.wap to check the given number is odd, if it is odd divide it by 2 and print reminder
#and quotient else print it is even (take user input)
num=eval(input('Enter the number : '))
if num%2==1:
    num/2
    print("reminder",num%2)
    print("quotient",num//2)
else:
    print("It is even.")


#18.wap to check if the given character is alphabet or Not ,if it is alphabet,
#create a replica of it 2 times. (take user input)
char=eval(input('Enter the Character : '))
if char.isalpha():
    print(char*2)
else:
    print(char)

    








































































































































































































































