Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#operators
#there are seven type of operators
#1.Arithematic
#2.Relational
#3.Logical
#4.Assignment
#5.Bitwise
#6.Membership
#7.Identity

#1.Arithematic Operators
#Addition(+)

2+3
5

2.5+3.5
6.0

(2+3j)+(7+5J)
(9+8j)

(2j+3)+(7+5J)
(10+7j)

[3,4]+[789+34]
[3, 4, 823]

'ape'+'ksha'
'apeksha'

{4:3}+{3:4}
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    {4:3}+{3:4}
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

(4,5)+(34,6)
(4, 5, 34, 6)

(0,54)+[4+4]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    (0,54)+[4+4]
TypeError: can only concatenate tuple (not "list") to tuple



#2.Subtraction Operator

45_45
4545

56-12
44

22.5-5.3
17.2

(7j)-(5+9j)
(-5-2j)

True-False
1

'jhkjgh'-'flhl'
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    'jhkjgh'-'flhl'
TypeError: unsupported operand type(s) for -: 'str' and 'str'

['gauri','aman']-['neha','piush']
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    ['gauri','aman']-['neha','piush']
TypeError: unsupported operand type(s) for -: 'list' and 'list'

('gauri','aman')-('neha','piush')
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    ('gauri','aman')-('neha','piush')
TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'

{45,18,7}-{10,7,19}
{18, 45}




#set subtraction behave like differnce method in

{'shivam','shruti','soham'}-{'khushi','sangameshvar','suraj'}
{'soham', 'shivam', 'shruti'}

#subtraction Operator
(2,3,4)-[3,4,5]
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    (2,3,4)-[3,4,5]
TypeError: unsupported operand type(s) for -: 'tuple' and 'list'

#subtraction operator only suppoet set .not list,string,dict,tuple



#Multiplication Operators
2*3
6
2.4*3.5
8.4

(2+3j)*(4+5j)
(-7+22j)

True*False
0

True*True
1

'Apeksha'*'Shruti'
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    'Apeksha'*'Shruti'
TypeError: can't multiply sequence by non-int of type 'str'

(2,4,5)*(3,45,5)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    (2,4,5)*(3,45,5)
TypeError: can't multiply sequence by non-int of type 'tuple'

{2,3,5}*{6,7,8}
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    {2,3,5}*{6,7,8}
TypeError: unsupported operand type(s) for *: 'set' and 'set'
[2,4,5]*[2,6,6]
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    [2,4,5]*[2,6,6]
TypeError: can't multiply sequence by non-int of type 'list'

45.5*8.6
391.3

'hii'*2
'hiihii'
#it will support duplicte
#opr1*n(n=int)

(2,3)*3
(2, 3, 2, 3, 2, 3)

[5,6,7]*2
[5, 6, 7, 5, 6, 7]

{3,4,6}*4
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    {3,4,6}*4
TypeError: unsupported operand type(s) for *: 'set' and 'int'




#Division
#1.True division
#2.floor division
#3.modulous division


18/4
4.5
#true-->question as result
#floor-->only int part from division
#modulous-->only remainder
#true-->question as result(/)
#floor-->only int part from division(//)
#modulous-->only remainder(%)
>>> 
>>> 
>>> 17//3
5
>>> 
>>> 17%3
2
>>> 
>>> 17/3
5.666666666666667
>>> 
>>> 
>>> 
>>> #power Operator
>>> #(**)
>>> 1**2
1
>>> 
>>> 4**2
16
>>> 
>>> 5**3
125
>>> 
>>> 5**4
625
>>> 
>>> 5**5
3125
>>> 
