#reversed()

''' inbuild function directly output is object addresss.'''


#difference between reverse and reversed
'''
reverse is used in stringg and reversed is a inbuikd function


in reversed to avoid object addreass data we have two ways --->

1.Typecasting
2.Looping


Typescasting  Syntax---->
                 

                      list(reversed(iterable))
                      tuple(reversed(iterable))
                      set(reversed(iterable))
                      dict(reversed(iterable))

Looping syntax---->

             for variable in reversed(iterable):
                                   statement
                                          '''
'''

s='python'
print(reversed(s))  #object addresss
print(list(reversed(s)))
                                          
for i in reversed(s):
      print(i,end=' ')
print()

res=' '
for i in s:
    res=i+res
    print(i)
'''


d=[1,2,3,4,5]
for i in reversed(d):
    print(i,end=' ')
print()

for i in d[::-1]:
    print(i,end=' ')
print()

for i in range(-1,len(d)-1,-1):
    print(d[i],end=' ')
print()

rev=[]
for i in d:
    rev=[i]+rev
print(rev)
print()
 
    
