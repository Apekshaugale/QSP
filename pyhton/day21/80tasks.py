'''
#1. Check Positive Number
num=eval(input("Enter the number : "))
if num>0:
    print(f'The number "{num}" is positive .')


#2. Check Negative Number
num=eval(input("Enter the number : "))
if num<0:
    print(f'The number "{num}" is Negative .')

#3. Check Zero
num=eval(input("Entre the number : "))
if num==0:
    print(f'The number  is zero.')


#4.Eligible to Vote
age=eval(input("Enter the age : "))
if age>=18 :
    print(f'Eligible to vote') 
    

#5. Driving License
age=eval(input("Enter the age : "))
if age>=18 :
    print('Eligible for Driving License.')

#6. Pass Student
marks=eval(input("Enter the marks secured :"))
if marks>=35:
    print('The student is Pass with "{marks}" marks.')

#7. Salary Eligible
salary=eval(input("Enter the salary : "))
if salary>=30000:
    print('The person is eligible for loan')

    
#8. Adult Person
age=eval(input("Enter the age of person : "))
if age>=18:
    print(f"The person of age {age} is Adult Person.")

#9. Temperature Check
temp=eval(input("Enter the temperature : "))
if temp>=32:
    print(f"The temperature {temp} is high.")
    

#10. ATM Balance
balance=eval(input('Enter the Balance :'))
if balance>0:
    print(f'The  ATM balance  is {balance}')


#11. Even Number
num=eval(input("Enter the number : "))
if num&1==0:
    print(f'The number "{num}" is even number.')

    
#12. Odd Number
num=eval(input("Enter the number: "))
if (num&1)!=0:
    print("The number is odd number.")
    
#13. Divisible by 5
num=eval(input("Enter the number :"))
if num%5==0:
    print(f'The number "{num}" is divisible by 5.')
    
#14. Divisible by 10

num=eval(input("enter the number : "))
if num%10==0:
    print(f'The number "{num}" is divisible by 10.')

#15. Divisible by 3
num=eval(input('Enter the number : '))
if num%3==0:
    print(f'The number "{num}" is divisible by 3.')

#16.Multiple of 7
num=eval(input("Enter the number : "))
if num%7==0:
    print(f'The number "{num}" is multiple of 7.')
    
#17. Check Leap Year
year=int(input('Enter the number : '))
if year%4==0:
    print(f'The year "{year}" is leap year .')

#18. Square Greater Than 100
num=int(input("Enter the number : "))
if (num**2)>100:
    print(f'The number "{num}" is greater than 100.')

  
#19. Cube Greater Than 500.
num=int(input("Enter the number : "))
if (num**3)>500:
    print(f'The number "{num}" is greater than 500.')
    
#.20. Number Ends with Zero.
num=int(input("Enter the number : "))
if num%10==0:
    print("The number ends with zero.")

    
  
#21. Empty String
a=str(input("Enter the string : "))
if ''==a:
    print('The given string "{string}" is empty .' )

#22. Name Starts with A
name=str(input("Enter the string : "))
if name[0]== "A":
    print(f'The given string "{name}"  starts with A .' )


#23. Name Ends with n
name=str(input("Enter the string : "))
if name[-1]=='n':
    print(f'The string "{name}" is ends with n .')

#24. Length Greater than


#25.check upper
name=str(input('Enter the string : '))
if name.isupper():
    print(f'The given  string "{name}" is in upper.')
    
#26.Check Lowercase 
name=str(input('Enter the string : '))
if name.islower():
    print(f'The given  string "{name}" is in lower.')

#27.Alphabet Only
name=str(input('Enter the string : '))
if name.isalpha():
    print(f'The given  string "{name}" contains alphabets.')

#28.Digit Only
name=eval(input('Enter the string : '))
if name.isdigit():
    print(f'The given  string "{name}" contains only digits.')    

#29.Alphanumeric
name=eval(input('Enter the string : '))
if name.isalnum():
    print(f'The given  string "{name}" contains alphabets and  digits.')    



#30.check space
name=str(input('Enter the string : '))
if name.isspace():
    print(f'The given  string "{name}" contains space.')    


#31.Check List Empty
list=eval(input('Enter the list : '))
if list==[]:
    print('The list is empty')


#32. List Length Greater Than 5
a=eval(input('Enter the list : '))
if len(a)>5:
    print(f'The length of "{a}" is greater than 5')


#33.Number Exists in List
num=eval(input('Enter the list : '))
if 9 in num:
    print(f'The number 9 is exists in list.')


    
#34.Largest Element Greater Than 100
element=eval(input('Enter the list : '))
if max(element)>100:
    print(f'The "{max(element)}" is greater than 100.')


#35.Smallest Element Less Than 0 Program
#x = [11, -5, 35, 507]
x=eval(input('Enter the list :'))
if min(x)<0:
    print(f'The min of x "{min(x)}" is less than 0.')

#36. list element Sum Greater Than 500
x=eval(input('Enter the list :'))
if sum(x)>500:
    print(f'The sum of elements is "{sum(x)}"  greater than 500.')
    

#38.wap to check age>18 and salary is greater than 30000 age = 25salary = 40000#and age>=25 and 4000>=300000
salary=eval(input('Enter the salary : '))
age=eval(input('Enter the age : '))
if salary>=40000 and age>=18:
    print( 'The person eligible for loan')


#39.wap to match Username and Password Match(user input)
admin='Apeksha'
username=eval(input('Enter the user name : '))
user_passward=6774
Passward=eval(input('Enter the passward : '))
if (username==admin) and (Passward==user_passward):
    print(' The username and passward is vaild.')

#40.wap to check Marks > 35 and Attendance > 75(take user iput)
marks=eval(input('Enter the marks : '))
attendance=eval(input('Enter the marks : '))
if marks>35 and attendance>75:
    print('The student eligible for exam.')

 
#41.wap to check the given number even and Positive
number=eval(input('Enter the number : '))
if number%2==0 and number>0:
    print(f'The given number "{number}" is even and positive')


#42.wap to check given Number Between 1 and 100
number=eval(input('Enter the number : '))
if number>0 and number<100:
    print(f'The number "{number}" is between 1 and 100.')

#43.wap to check the given number Divisible by 3 and 5
number=eval(input('Enter the number : '))
if number%3==0 and number%5==0:
  print('The given number is divisible by 3 and 5')


#44.wap to check the given number Divisible by 2 or 7
number=eval(input('Enter the number : '))
if number%2==0 and number%7==0:
  print('The given number is divisible by 2 and 7')


 
#45.wap to check Name Starts with A and Ends with a name="Anita"
name=eval(input('Enter the Name : '))
if name[0]=='A' and name[-1]=='a':
    print(f'The name "{name}" is starts with A and ends with a .')


#46.wap to check Salary > 50000 or Experience > 5
Salary=eval(input('Enter the salary :'))
Experience=eval(input('Enter the experience :'))
if Salary>50000 or Experience >5:
    print('The person is eliglible for Senoir Role.')


#47.wap to check Temperature > 35 and Humidity > 80
Temperature=eval(input('Enter the temperature :'))
Humidity=eval(input('Enter the humidity :'))
if Temperature>35 and Humidity>80:
    print('The Climate is not good for health.')



#48.wap to check if the student has scored 70% print "good luck "(take user input)
marks=eval(input('Enter the marks : '))
if marks>=70:
    print('Good Luck.')

   
#49.wap to check which number is greater using if condition
#a=98
#b=67
a = int(input("Enter first number: "))
b = int(input("Enter second number : "))
if a > b:
    print(f"{a} is greater than {b}.")


#50.wap to check if the given string has even length of character
s="hey guys you all are Osam"
if len(s)%2==0:
    print('The string has even length of character')

s=eval(input('Enter the string '))
if len(s)%2==0:
    print('The string has even length of character')

#51.wap to check if the given number is divisible by 5 (take user input)
num=eval(input('Enter the number : '))
if num%5==0:
    print(f'The number "{num}" is divisible by 5.')

#52.wap to check if the given programming is present in the list

p=["java","python","c","c++","RUBy","golang"]
if "java" in p:
    print('The given programming is present in the list.')

   
#53.wap to check eligible to vote take user input as a age.
age=eval(input('Enter the age : '))
if age>18:
    print('The person is eilgible for vote.')

    

#55.wap to check if the given string is palindrome (take user input)
string=eval(input('Enter the string : '))
if string[::-1]==string:
    print('The given string is palindrome.')

    

#56.wap to check if the first letter in the given string is consonant##if s[0] not in 'a,e,i,o,u':

s="Lahari is a good student"
if s[0]not in 'aeiouAEIOU':
    print('The first letter in the given string is consonant')

#57.wap to check the given string is uppercase or not (take user input
string=eval(input('Enter the string : '))
if string.isupper():
    print('The given string is in upper.')

    
#58.wap to check the given value is string (take user input)
string=eval(input('Enter the string : '))
if type(string)==str:
    print('The given value is string.')

#59.wap to display "Python Coding" if the number is greater than 1 and less than 5 (take user input)
num=eval(input('Enter the string : '))
if num>1 and num<5:
    print('Pyhton Coding.')


    
#60.wap to check whether given number is negative and print "its negative guys"
num=eval(input('Enter the string : '))
if num<0:
    print("Its negative guys")


#61.wap to check whether given input is divisible by 2 and 6 if condition is True ,convert the given number to complex number.(take user input)
number=eval(input('Enter the number : '))
if number%2==0 and number%6==0:
  print(complex(number))



#62.wap to check whether the given number is even or not, if even store the value inside the list (take user input)
number=eval(input('Enter the number : '))
x=[]
if number%2==0:
    x.append(number)
    print(x)


#63.wap to check whether a given value is divisible by 5 and 7,if the value is divisible then display the square of the values (take user input)
number=eval(input('Enter the number : '))
if number%5==0 and number%7==0:
  print('The square of given value is',number**2)

  

#64.wap to check whether a given value is present in between 45 and 200 and the number should be divisible by 4 and 5
#,if satisfied, display the ascii characters (take user input)
value=eval(input('Enter the value : '))
if (value>45 and value<200) and (value%4==0 and value%5==0):
    print(f'The ASCII character of given value "{value}" is ',chr(value))

    

#65.wap to checking if a string contains a substring

string="hello world"
if 'world' in string:
    print(f'The given string "{string}" contains subtraing "world".')


string=eval(input('Enter the string : '))
if 'world' in string:
    print(f'The given string "{string}" contains subtraing "world".')

    
#66.wap to check whether a character is in the alphabet or not,if it is alphabet, store the value inside
#a dict(key as a character and value as a ascii value)
character=eval(input('Enter the character : '))
x={}
if character.isalpha():
    print(f'The given character "{character}" is in alphabet.')
    x[character]=ord(character)
    print(x)
    

#67.wap to check whether a character is in uppercase or not,
#if uppercase, convert to lowercase and store the value inside the dictionary
#(character as key and ascii as value) take user input
character=eval(input('Enter the character : '))
dictionary={}
if character.isupper():
    print(f'The given character "{character}"  in lowercase = ',character.lower())
    dictionary[character]=ord(character)
    print(dictionary)

#68.Write a program to check if a string ends with a period ('.').
string=eval(input('Enter the string: '))
if string[-1]==".":
    print('string ends with a period .')

  

#69.  Write a program to check if 'a' is present in the string s = 'apple'.
s = 'apple'
if "a" in s:
    print("'a' is present in the string")



#70.  Write a program to check if the first and last characters of a string are the same (e.g., x = 'level').

string=eval(input('Enter the string: '))
if string[0]==string[-1]:
    print('The first and last characters of a string are the same')

    

#71.  Write a program to check if a character is a vowel. (e.g., a = 'I')
string=eval(input('Enter the character: '))
if  string in 'aeiouAEIOU':
    print(f'"{ string}"=character is a vowel')

    
#72.Write a program to check if a character is uppercase. (e.g., b = 'P')
b=eval(input('Enter the character: '))
if  b.isupper():
    print(f'character "{ b}"  is a uppercase character.')




#73.  Write a program to check if a character is lowercase. (e.g., c = 'k')
a=eval(input('Enter the character: '))
if  a.islower():
    print(f'character "{a}"  is a lowercase character.')


    
#75.  Write a program to check if the ASCII value of a character is greater than 100. (e.g., z = 'd')#if ord("z")>100
character=eval(input('Enter the character : '))
if ord(character)>100:
    print(f"The ASCII value of '{character}' is greater than 100.")


#77.  Write a program to check if the last element in a list is even. (e.g., l = [1, 2, 4])#l[-1]%2==0

list=eval(input('Enter the element: '))
if list[-1]%2==0:
    print(f'The last number "{list[-1]}" is even.')



#78.Allow withdrawal only if the balance is sufficient.
balance = 10000
#if b >w:
withdraw=eval(input('Enter the amount : '))
if balance>=withdraw:
    print('You can withdraw money ')

    
#79.Login only if the username and password are correct.
username="apeksha"
passward=1234
uname=eval(input('Enter the username : '))
pword=eval(input('Enter the password : '))
if username==uname and   passward==pword:
    print('Login successful.')

#80.Verify the entered OTP.

otp = 4567
#entered = 4567

entered=eval(input('Enter the otp : '))
if otp==entered :
    print('Verified successful.')

   

#81.Book a ticket only if seats are available.
seats=15
if seats>0:
    print("Book a ticket")

     
#85.Students with 75% or more attendance can write the exam.
#attendance = 82
Attendance=eval(input('Enter the Attendance : '))
if Attendance>=75:
    print('Student can write an exam.')


#86.Employees with more than 5 years of experience receive a bonus
#experience=6
exp=eval(input('Enter the Experience : '))
if exp>5:
    print(f'The employee has "{exp}" years of experience can receive a bonus.')

    
#87.Customers receive a discount if they spend ₹5,000 or more.
bill=eval(input('Enter the amount of bill : '))
if bill>=5000:
    print('Eligible for discount.')
    

#88. Write a program to check if a credit card number is 16 digits and contains only digits. (e.g., cc = '1234567812345678')#if len(cc)==16 and cc.isdigit:
card=eval(input('Enter the credit card number : '))
if len(card)==16 and card.isdigit():
    print('The given card number is correct.')

    '''


#90.Write a program to check if the given string is a palindrome. (Take user input)
string=eval(input('Enter the character: '))
if string[::-1]==string:
    print('The given string is a palindrome.')

