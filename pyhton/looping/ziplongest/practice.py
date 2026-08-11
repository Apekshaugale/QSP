#Print odd numbers from 1 to 20.
'''for i in range(1,21):
    if i%2==1:
        print(i,end=' ')
'''
#Print numbers from 20 to 1.
'''for i in range(21,1,-1):
   
        print(i,end=' ')

#Print the multiplication table of 7.
for i in range(1,11):
    print(i*7,end='  ')


#Print each character of "hello" along with its index.
s='hello'
for i in enumerate(s):
    print(i)


#Print index and character only for characters at even indexes.
s = "python"
for i ,j in enumerate(s):
    if i%2==0:
        print(i,j)
#Create index-character pairs.
s = "hello"
a=[]
for i in enumerate(s):
    a.append(i)
print(a)

s = "hello"
a=[]
for i in enumerate(s):
    a=a+[i]
print(a)



#Print only characters whose index is greater than 2.
s = "programming"
for i,j in enumerate(s):
    if i >2:
       print(j,end=' ')

s = "programming"
for i in enumerate(s):
   
       print(i,end=' ')
'''
s = "programming"
print(list(enumerate(s)))


a=[10,20,30]
b=[30,30]
for i in zip(a,b):
    print(i,end=' ',fillvalue=None)
