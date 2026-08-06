'''25.wap to print the count of alphabets and numbers and space in the given string

s="india got the independence in the year 1947"
num=0
alpha=0
space=0
for a in s:
    if a.isalpha():
        alpha=alpha+1   
    elif a.isdigit():
         num=num+1
    else:
     space=space+1
print(alpha)
print(num)
print(space)
'''

'''24.wap to extract only individual data types from the list and sum all the individual data types

l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
data=0
for s in l:
    if isinstance(s,(int,float,bool,complex)):
        print(s)
        data=data+s
print('Sum of individual data type is  : ',data)
'''
'''
a=[52,455,56]
b=0
for i in a:
    b=b+i
print(b)

'''
'''23.wap to extract only individual data types form the list

l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
for a in l:
    if isinstance(a,(int,float,bool,complex)):
        print(a)
'''

'''22.wap to capitalize only the first letter of every word in the given list

l=["vaidegi","rahul","shivam","kapil","patil"]
for a in l:
    print(a.capitalize(),end='  , ')
    '''

'''21.wap to extract vowels and digits in a string

s="hello123"
for a in s:
    if a in 'aeiouAEIOU' or a.isdigit():
            print(a,end='  ')

'''
'''
20.wap to print the number form 1 -20 segregate even and odd number into list 
even = []
odd = []
for a in range(1, 21):
    if a % 2 == 0:
        even.append(a)
    else:
        odd.append(a)

print("Even numbers:", even)
print("Odd numbers:", odd)
'''


'''19.Sum of even numbers
e=[1,2,3,4,5,6,7,8]
b=0
for a in e :
    if a%2==0:
        print(a)
        b=b+a
print('sum of even number is ',b)
'''

'''18.wap to Separate even/odd

e=[1,2,3,4,5,6,7,8]
a=[]
b=[]
for i in e:
    if i%2==0:
        a=a+[i]       
    else:
        b=b+[i]
print("Even numbers:", a)
print("Odd numbers:", b)'''


'''17.Count positive numbers

l = [-1,4,-3,7,9]
char=0
for i in l:
    if i>0:
        char=char+i
        print(i)
print('Count of positive number is : ',char)
'''

'''16.Print numbers greater than 50
l = [23,67,12,89,54]

for a in l:
    if a>50:
        print(a,end='  ')

        '''

'''15.wap to Count consonants

s = "education"
char=0
for a in s:
    if a not in 'aeiouAEIOU':
        char=char+1
print(char)
        
'''
''' 14.Print ASCII values of characters
s='ABC'
for i in s:
    print(i,ord(i))
'''

'''13.Squares from 1 to 10
for i in range(1,11,1):
    print(i,i**2)
   '''

'''12.Reverse 10 to 1
for i in range(10,0,-1):
    print(i,end=' ' )
    '''

''' 11.wap Print numbers divisible by 5 (1 to 51)
 
for i in range(1,52,1):
    if i%2==0:
      print(i,end=' ' )

'''

''' 10.wap Sum from 1 to 50
  
s=0
for i in range(1,51,1):
     s=s+i
print('sum of number from 1 to 50 is : ',s )
'''

'''9.Print odd numbers 1 to 20 
for i in range(1,21,1):
     if i%2==1:
          print('odd  number from 1 to 20 is : ', i)

'''

'''8.Count odd numbers

l = [1,2,3,4,5,6,7]
char=0
for i in l:
    if i%2==1:
        print(i)
        char=char+1
print('Count odd numbers is : ',char)
'''

'''7.Print negative numbers 
l = [4,-2,7,-9,3]
for i in l:
    if i<0:
        print(i,end=' ')
        '''
'''  6.Print even numbers from list 
e=[23,45,66,78,90]
for i in e:
    if i %2==0:
       print(i,end=' ') '''

'''5.Sum of list elements
x=[25,70,90,100]
s=0
for i in x:
    s=s+i
print('Sum of list elements: ',s)
'''

'''4.Print digits from string

s = "ab12cd34"
for a in s:
    if a.isdigit():
        print(a,end='  ')
'''
'''3.Count uppercase letters'''
s = "PyTHon"
c=0
for a in s:
    if a.isupper():
        c=c+1
        print(a,end='  ')
print('count of uppercase letter: ',c)

''' 2.Print vowels only
s = "education"
for a in s:
    if a in 'aeiouAEIOU':
        print(a,end='  ')
'''
'''1. Print each character of a string
a="Tree Notes"
for i in a:
    print(i,end='  ')
'''
