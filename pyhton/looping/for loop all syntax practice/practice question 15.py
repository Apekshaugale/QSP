'''1.WAP to return a dictionary with word & its len pair
#from a string
string = 'hello good morning how are youu'
#exp o/p : {hello:5, guys:4, morning:7, how:3, are:3, you:4}

string = 'hello good morning how are you'
d={}
for i in string.split(' '):
  d[i]=len(i)
print(d)


d={}
for i in string.split(' '):
  d.update({i:len(i)})
print(d)


'''

"""
2.WAP to count number of vowels present in given string
s = 'GooD mOrnIng'

count=0
s = 'GooD mOrnIng'
for i in s:
   if i in "aeiouAEIOU":
       count=count+1
print('count of   vowels number = ',count)

"""

"""
3.WAP to get below o/p:

#exp o/p : 'iH woh era '

s = 'Hi how are you'

for i in s.split(' '):
    
    print(i[::-1],end='  ')

res=' '
for i in s.split(' '):
    res=res+' '+i[::-1]
print(res)
"""
"""
4.WAP to print all the digits in a below list
l = ['hello', '123', 'hai', 'python', '345']
for i in l:
    if i.isdigit():
        print(i,end=' ')
        

"""


"""
5.WAP to check whether string is ANAGRAM or not
#sorted will work on ascii charcter it will work always asc to desc .written type is list.
#anagrams : characters should be same it can different meaning
#tea, eat
#silent, listen
#bored , robed
#cat, act
#keep, peek
#lamp, palm
"""
"""
a= 'tea'
b='eat'
print(sorted(a))
print(sorted(b))
if sorted(a)==sorted(b):
    print('its a anagram')
else:
    print('its not  anagram')

a= 'tea'
b='ate'
print(sorted(a))
print(sorted(b))
if sorted(a)==sorted(b):
    print('its a anagram')
else:
    print('its not  anagram') 


#silent, listen
a='silent'
b='listen'
if sorted(a)==sorted(b):
   print('its a anagram')
else:
    print('its not  anagram') """

#bored , robed
a='bored'
b='robed'
if sorted(a)==sorted(b):
    print('Its a anagram')
else:
    print('Its not a anagram')


#cat, act

a='cat'
b='act'
if sorted(a)==sorted(b):
    print('Its a anagram')
else:
    print('Its not a anagram')
#keep, peek
a='keep'
b='peek'
if sorted(a)==sorted(b):
    print('Its a anagram')
else:
    print('Its not a anagram')
#lamp, palm
a='lamp'
b='palm
if sorted(a)==sorted(b):
    print('Its a anagram')
else:
    print('Its not a anagram')


"""
6.Find the sum of even numbers from 1 to 20

s=0
for i in range(1,21):
    if i%2==0:
        s=s+i
        print(i)
print('sum of even number from 1 to 20 = ',s)
"""

'''

#7.Count numbers divisible by 3 from 1 to 50
s=0
for i in range(1,51):
    if i%3==0:
        s=s+i
        print(i)
print('sum of even number from 1 to 50 = ',s)
'''



"""
#8.Replace negative numbers with 0
numbers = [10, -5, 20, -3, 40]


num= [10, -5, 20, -3, 40]
for i in range(len(num)):
    if num[i] <0:
        num=0
print(num)
"""
"""


#9.Print position of each character
word = "PYTHON"
"""
"""
1 P
2 Y
3 T
4 H
5 O
6 N

word = "PYTHON"
for i in enumerate(word,start=1):
    print(i)
    
"""

'''
#10.Count even and odd numbers in a list.
num= [10, 15, 22, 31, 40, 
even=0
odd=0
num= [10, 15, 22, 31, 40, 51]
for i in num:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print(even)
print(odd)
'''

'''

#11.wap to print repeated char and count the same'''
'''s="helloworld"
count=0
rev=' '
for i in s:
    if s.count(i)>1:
        count=count+1
          if i not in rev:
            
            rev=rev+i
            print(count,i)

'''
            

'''
for i in s:
    if s.count(i) > 1 and s.index(i) == s.index(i):
        if i not in s[:s.index(i)]:
            print(i, s.count(i))'''
'''
#12.Grouping flowers and animals separately
flower=[]
animals=[]
items=["lotus-flower","lilly-flower","cat-animal","dog-animal","sunflower-flower"]
for i in items:
    
    if  i.endswith('-flower'):
         flower.append(i)
    else:
       animals.append(i)
print(flower)
print(animals)
'''
'''
#13.filter only character except digits
s="Think456 and 123answers it789 guys "
for i in s:
    if i.isalpha():
        print(i,end=' ')
        
for i in s.split():
    if i.isalpha():
        print(i,end=' ')
'''
'''
#14.replace whitespaces with newline char in the below string

s = "hello world welcome to python"

for i in s:
    if i == ' ':
        print('\n', end='')
    else:
        print(i, end='')
        '''
'''
#15.replace all vowels with *
s="hello world welcome to python"

s="hello world welcome to python"
a=' '
for i in s:
    if i in'aeiouAEIOU':
        
        a=a+'*'
    else:
        a=a+i
print(a)
    '''    


'''

#wap to check guve number is armstrong number or not
a=153
total=0
b=str(a)#153--->'153'
print(b)#---->iterable
power=len(b)
print(power)
for i in b:
    total=total+int(i)**power
    print('total =',total)
if total==a:
    print('Its a armstromg number')
else:
    print('Its not a armstromg number')
'''
'''
#wap to write a table from2 to 10 numbers
for i in range(1,11):
    for j in range(2,11):
        print(i*j,end=' ')
    print()


for i in range(1,11):
    for j in range(1,11):
        print(f'{i}*{j}----> {i*j}')
    print()

 '''
'''
s='good morining'
for i in enumerate(s,start=2):
    print(i,end=' ')

for vqariable in enumerate(iterable,start=number):
     statement

'''
