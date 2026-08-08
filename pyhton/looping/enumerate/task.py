'''30.wap to create a dictionary with element and its count pair

output:-->
{'yellow': 2, 'red': 2, 'black': 1, 'pink': 2, 'orange': 1, 'green': 1}

l=["yellow","red","black","pink","orange","green","red","pink","yellow"]
d={}
count=0
for i in l:
    count=count+1
    d[i]=count
print(d)
'''

'''
d = {}

for i in l:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1

print(d)
'''
'''
31.wap to find the length of the string without using inbuilt function
s="Never Give Up"
count=0
for i in s:
    count=count+1
print(count)

'''

'''33.wap to reverse a string without using inbuilt function
x="you did it guys"
for i in x[::-1]:
    print(i,end= ' ')

rev=
'''

''''33.wap to print alternative character from a given string
s='hello python'
for i in range(0,len(s),2):
    print(s[i],end=' ')
'''


'''
a='123456789'
even=''
odd=''
for i in range(1,10,1):
    if i%2==0:
        even=even+str(i)
    elif i%2==1 :
        odd=odd+str(i)
print(even,end='')      
print(odd,end='')
'''
'''34.wap to create a dictionary index and word pair
o/p:-->{0: 'tomorrow', 1: 'is', 2: 'weekend', 3: 'and', 4: 'non-veg', 5: 'special'}'''

s="tomorrow is weekend and non-veg special"
a={}
for i in s.split():
    a[i]=ord(i)
    print(i)
print(count)

