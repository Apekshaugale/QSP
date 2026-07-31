'''
WAP to check whether a given value is a list and first and last values should be
integer if condition is satisfied first value is True division by 3 and perform the
bitwise not for last value and those result values are stored in same positions in
given list or else, to perform length of the collection power by 2 and display
value.'''
'''
a=eval(input('Enter the list'))
if isinstance(a,list) and isinstance(a[-1],int) and isinstance(a[0],int):
    a[0]=a[0]/3
    a[-1]=~a[-1]   #n=-(n+1)
    print(a)
else:
    print(len(a)**2)
'''

'''
WAP to check whether a given value is a string or not and length of the value
should be more than 7, if condition is satisfied to append the new string in the
middle of the given string or else to perform the replications with 3 and display
the result.'''
'''
s=eval(input('Enter the string'))
low=0
high=len(s)-1
if isinstance(s,str) and len(s)>7:
    sub_string=eval(input('insert the data'))
    mid=(low+high)//2
    data=s[:mid:]+sub_string+s[mid::]
    print(data)
else:
    print(a*3)
''' '''
OR

d='Morningclass'
e='777'
if type(d) and len(d)>7:
    mid=(len(d))//2   #low+high//2
    data =d[:mid:]+e+d[mid::]
    print(data)
else:
    print(d*3)

    '''
'''
WAP to check if the given string of first and second character should be sequence
or not. if the sequence prints the first, second and last two characters, or else the
first half string is reversed and the remaining half string should be normal and
display it'''
'''
x=eval(input('Enter the data:'))
low=0
high=len(x)-1
#xyz are sequence
if (ord(x[0]) +1==ord(x[1])):
    print("first",x[0])
    print("second",x[1])
    print("last two",x[-2:])
else:
    mid=(low+high)//2
    print(mid)
    data=x[0:mid+1:][::-1]+x[mid+1::]  #for reversing the string we use [0:mid+1:][::-1]
    print(data)
    
    '''

'''WAP to check whether a given key is present in the dict or not. if key is present:
display the value or else add key and new value inside the dict'''
'''
value=eval(input('Enter the value  : '))
if   value%2==0 and 65<=value<=90 :
    print(chr(value))
else:
    print(value//5)

'''
'''
s=eval(input('Enter the string:'))   

if len(s) > 10 and (ord(s[0]) + ord(s[-1])) % 5 == 0:
    print('first character : ',ord(s[0]))
    print('middle character :',ord(s[(len(s)-1)//2]))
    print('last character :',ord(s[-1]))
else:
    print(s*3)
'''
'''


