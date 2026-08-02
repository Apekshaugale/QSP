'''1.WAP to check whether a given number is divisible by 3 and 5.If the number is divisible by 3 print Fizz,
if the number divisible by 5 print 'buzz' if it divisible by both then print fizz buzz 
num=eval(input('Enter the number : '))
if num%3==0 and num%5==0:
    print('Fizz Buzz')
elif num%5==0:
    print('Buzz')
elif num%3==0:
    print('Fizz')
'''


'''2.WAP to check if a given number is one digit or two digit or three digit or more than 3 digit.
If one digit display the one digit, if two digit display the two digit value and so on. 
num=eval(input('Enter the number : '))
if len(str(num))==1:
    print(f'One digit value is "{num}".')
elif len(str(num))==2:
    print(f'Two digit value is "{num}".')
elif len(str(num))==3:
    print(f'Three  digit value is "{num}".')
elif len(str(num))>3:
    print(f'More than three   digit value is "{num}".')
'''

'''3.WAP to accept any number from 1-5 and display that number is word form 
num=eval(input('Enter the number : '))
if num==1:
    print(f'"{num}"=One.')
elif num==2:
    print(f'"{num}"=Two .')
elif num==3:
    print(f'"{num}"=Three .')
elif num==4:
    print(f'"{num}"=Four.')
elif num==5:
    print(f'"{num}"=Five.')
else:
    print("Please enter a number between 1 and 5.")


'''

'''4.WAP to check ''whether a given character is uppercase or lowercase or special character.
if uppercase convert to lowercase or leif lowercase, conver into upper or
else display the [revious, given and next characters and display it.]

#without inbuild function

char=eval(input('Enter the character :'))
if ord('A')<=ord(char)<=ord('Z'):
    print(f'The given uppercase character is  "{char}" into  lowercase is "{char.lower()}".')
    print('previous charcter = ',chr(ord(char)-1))
    print('Next charcter = ',chr(ord(char)+1))
elif ord('a')<=ord(char)<=ord('z'):
    print(f'The given lowercase character is  "{char}" into  uppercase is "{char.upper()}".')
    print('previous'' charcter = ',chr(ord(char)-1))
    print('Next charcter = ',chr(ord(char)+1))
else:
    print(f'The given character is  "{char}" is special character .')
    print('previous charcter = ',chr(ord(char)-1))
    print('Next charcter = ',chr(ord(char)+1))
 '''
'''
#with inbuild function

char=eval(input('Enter the character :'))
if char.isupper():
    print(f'The given uppercase character is  "{char}" into  lowercase is "{char.lower()}".')
    print('previous charcter = ',chr(ord(char)-1))
    print('Next charcter = ',chr(ord(char)+1))
elif char.islower():
    print(f'The given lowercase character is  "{char}" into  uppercase is "{char.upper()}".')
    print('previous charcter = ',chr(ord(char)-1))
    print('Next charcter = ',chr(ord(char)+1))
else:
    print(f'The given character is  "{char}" is special character .')
    print('previous charcter = ',chr(ord(char)-1))
    print('Next charcter = ',chr(ord(char)+1))
'''

'''4.wap  to check given Password length is lessthan 6 print week and
length is in between 6 to 8 medium else password length is
9 to 12 strong above print verystrong 
p=eval(input('Enter the passward : '))
if len(str(p))<6:
    print('Weak ')
elif 6<=len(str(p))<=8:
    print('Medium')
elif 9<=len(str(p))<=12:
    print('Strong')
else:
    print('VeryStrong')
    '''


'''5.Create a Login System:

Correct username and password → Login Successful
Correct username, wrong password → Incorrect Password
Wrong username → User Not Found 
uname='Apeksha'
pword='123@45'
username=eval(input('Enter the username :'))
password=eval(input('Enter the password : '))
if username==uname and password==pword:
    print('LOGIN SUCCESSFUL')
elif username==uname and password!=pword:
    print('Incorrect Password .')
elif username!=uname :
    print('User Not Found .')

    '''

'''6.WAP to classify a given number. If the number is positive and even,
print "Positive Even". Else if it is positive and odd, print "Positive Odd".
Else if it is negative and even, print "Negative Even".
Else if it is negative and odd, print "Negative Odd". Otherwise, print "Zero". 


num=eval(input('Enter the number : '))
if num>0 and num%2==0:
    print("Positive Even")
elif num>0 and num%2!=0:
    print("Positive Odd")
elif  num<0 and num&1==0:
    print("Negative Even")
elif  num<0 and num&1==1:
    print("Negative Odd  ")
else:
    print("Zero")

'''

'''7.WAP to build a simple menu-driven food ordering system.
Accept a menu number from the user and display the corresponding food item
along with its price. If the entered menu number is invalid, print "Invalid Menu". 
num=eval(input('Enter the menu number : '))
if num==1:
    print(f'Menu {num}.Idli    Rs.40 ')
elif num==2:
    print(f'Menu {num}.Poha   Rs.25 ')
elif num==3:
    print(f'Menu {num}.Tea    Rs.15')
elif num==4:
    print(f'Menu {num}.Cold Coffee   Rs.40 ')
elif num==5:
    print(f'Menu {num}.Hot Coffee  Rs.20 ')
elif num==6:
    print(f'Menu {num}.Dosa    Rs.50 ')
elif num==7:
    print(f'Menu {num}.Noodles    Rs.70 ')
else:
    print(f'Menu {num} is Invaild. ')
    '''

'''8.WAP to check the teacher's mood based on the percentage of assignments submitted
by the class.Conditions:If 100% of the assignments are submitted,
print "Teacher is Very Happy ".Else if the percentage is between 75% and 99%,
print "Teacher is Happy     ".Else if the percentage is between 50% and 74%,
print "Teacher is Angry   ".Otherwise (below 50%), print "Surprise Test Tomorrow!  " 
num=eval(input('Enter the assignments submitted number : '))
if num==100:
    print( "Teacher is Very Happy ")
elif 75<=num<=99:
    print("Teacher is Happy     ")
elif 50<=num<=74:
    print("Teacher is Angry   ")
elif num<50:
    print("Surprise Test Tomorrow!  ")
'''


'''9.WAP to suggest a weekend plan based on the user's money and mobile battery percentage.

Money ≥ ₹1000 and Battery ≥ 80% → Go on a Trip 🏖️
Money ≥ ₹500 and Battery ≥ 50% → Watch a Movie 🍿
Money ≥ ₹200 and Battery ≥ 20% → Go to a Café ☕
Otherwise → Stay Home and Study Python 🐍 
Money=eval(input('Enter the Money  RS : '))
Battery=eval(input('Enter the Battery  %: '))

if Money >= 1000 and Battery >= 80 :
    print('Go on a Trip 🏖')
elif Money >= 500 and Battery >=50:
    print('Watch a Movie 🍿')
elif Money >=200 and Battery >= 20:
    print('Go to a Café ☕')
else:
    print('Stay Home and Study Python 🐍')

    '''
'''10.
