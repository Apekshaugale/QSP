#LOOPING:
'''
Set of instruction it will execute again and again  untill condition become False.


LOOPING TYPES---->


1.for loop

2.while loop


'''
'''
1.for loop:
  when we know the number of iterations (repetation)

  In for loop increament amd decrement it will appened internally .(we don't have to perform manually)




  Syntax--->
  for varibale  in iterable :
      statement



      where:
      1.for : keyword,it is start thhe code
      2.variable : startpoint
      3.if you miss 1 tab space you will get indentation error.
      4.ststement: block of code.
      5.in: it is a operator
      6. iterable : any multi value data type

'''
      # there are 8 syntax in for loop
'''
1.traveesing syntax
2.range
3.reversed
4.enuerate
5.zip
6.zip-longest
7.sorted
8.dyault dict
'''
#1.traversing syntax
'''      Syntax--->
  for varibale  in iterable :
      statement
      '''

a='Morining'

for i in a :
    print(i,end='  ')
b=[10,20,30,40,50]
print()
##empty print function is used to go in next line.
'''
c=(99,'lmli',65)
d={12:90,100:200,54:'abc'}
for i in d:
    print(i,'---->',d[i])

    print(d[i])
    print(d.items)
'''
'''
d={12:90,100:200,54:'abc'}
for i in d.items():
    print(i)
    print()
for i in d.values():
    print(i)
    print()
for i in d.keys():
    print(i)
    print()
'''


a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
    if i%2==0:
        print(i)
s=['abc','pyhton','java','sql','xyz']
for i in s:
    print(i.upper())

    print()
for i in s:
    print(i,i[0],i[-1])


s='pythhon231'
for i in s:
    if i.isdigit():
        print(i,end=' ')
        print()

s='Good Luck'
for i in s:
    if i not in 'aeiouAEIOU':
        print(i)
       
        
    

    
        
    
