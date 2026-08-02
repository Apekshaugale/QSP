'''
wap to check the given charcter is alphabet,digit,special charcter.
'''
'''
num=eval(input('Enyter the number'))
if num>0:
    print('it is  a +ve number.')
    
elif num==0:
    print('it is a neutral number.')
    
elif num<0:
    print('it is a -ve number.')

else:
    print('it is a -ve number.')
  '''


''' wap program to check givrn charcter is alphabet ,digit,special character
char=eval(input('Enter the charcter'))
if char.isdigit() :
    print('it is  a digit.')
    
elif char.isalpha():
    print('it is alphabet.')
    
else:
    print('it is a special caharcter.')

'''



'''wap program to check givrn charcter is uppercase ,lowercase,digit,without inbuild.

char=eval(input('Enter the charcter'))
if ord("A")<=ord(char)<=ord('Z') :                   #65<=char<=90 we can pass only single single character in it if we want to pass multiple chacter we use inbuiltfunction method
    print('it is  a uppercase.')
    
elif  ord("a")<=ord(char)<=ord('z') :  #97<=char<=122
    print('it is a lowercase.')
    
else:
    print('it is a digit.')   #elif ord("0")<=ord(char)<=ord('9') :


#OR

    #withinbuilt function.

char=eval(input('Enter the charcter'))
if char.isupper() :                   #65<=char<=90
    print('it is  a uppercase.')
    
elif  char.islower() :  #97<=char<=122
    print('it is a lowercase.')
    
elif char.isdigit():
    print('it is a digit.')
'''



'''wap to prrint based on number print number day
num=eval(input('Enter the number : '))
if num==1:
    print('Monday .')
elif num==2:
    print('Tuesday..')
elif num==3:
    print('Wwdnesday..')
elif num==4:
    print('Thrusday.')
elif num==5:
    print('Friday..')
elif num==6:
    print('Saturday..')
elif num==7:
    print('Sunday..')
else:
    print('Invaild number')

'''

'''wap to perform operation on number using symbol as input.
a=eval(input('Enter the number1 : '))
b=eval(input('Enter the number 2 : '))
ope=eval(input('Enter the operator: '))
if ope=='+':
    print(a+b)
elif ope=='-':
    print(a-b)
elif ope=='*':
    print(a*b)
elif ope=='/':
    print(a/b)
elif ope=='//':
    print(a//b)
elif ope=='%':
    print(a%b)
elif ope=='**':
    print(a**b)    
else:
    print('Invaild Opertaion')

'''

'''wap to check grater than 3 number which is greater 
a=eval(input('Enter the number1 : '))
b=eval(input('Enter the number 2 : '))
c=eval(input('Enter the number 3 : '))
if a>b and a>c:
    print(f"The greater number among '{b} ' and '{c}'  is ",a)
elif b>a and b>c:
    print(f"The greater number  among '{a} ' and '{c}'  is ",b)
else:
    print(f"The greater number  among '{a} ' and '{b}'  is ",c)

'''
'''wap to check samller than 3 number which is smaller
a=eval(input('Enter the number1 : '))
b=eval(input('Enter the number 2 : '))
c=eval(input('Enter the number 3 : '))
if a<b and a<c:
    print(f"The smaller number among '{b} ' and '{c}'  is ",a)
elif b<a and b<c:
    print(f"The  smaller number  among '{a} ' and '{c}'  is ",b)
else:
    print(f"The  smaller  number  among '{a} ' and '{b}'  is ",c)

'''
'''wap to check  according to age marriage condtionis 
a=eval(input('Enter the age : '))

if a<17:
    print(f"The Child Marriage.")
elif a==18:
    print(f"Eligible for Marrigae ")
elif 18<=a<=25:
    print(f"Love Marriage ")
elif 25<=a<=30:
    print('Arrange Marriage')
elif 30<=a<=40:
    print('Your choice')
    

'''
'''
2.wap to check a data is a sequence/iterable/individual data type'''
'''a=eval(input('Enter the data .'))
if isinstance(a,(tuple,str,list)):
    print('It is sequence data type.')
elif isinstance(a,(str,list,tuple,set,dict)):
    print('It is iterable  data type.')
elif isinstance(a,(int,float,bool,complex)):
        print('It is individual  data type.')'''


'''3.wap if input is string return its length,else if input is list pop element,else
 if input is tuple reverse else invalid input
a=eval(input('Enter the data .'))
if isinstance(a,(str)):
    print(len(a))
elif   isinstance(a,(list)):
    print(a.pop(0))
elif isinstance(a,(tuple)):
    print(a.reverse())
    '''


num = eval(input('Enter the number: '))

if num & 1 == 0:
    print(f'{num} is even. Odd number is {num + 1}')
else:
    print(f'{num} is odd. Even number is {num - 1}')






