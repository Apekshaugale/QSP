Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Logical Operator-->
#there are three type

#logical And
#logical OR
#logical Not

#all logical operators are keywords

#1.logical and

#it will perform logical and operation for the given operand
#syntax-->op1 and op2

(1,) and 'shruu'
'shruu'

True and False
False

90 and 56
56

(3.4j)and (3j)
3j

(3)and (3.4j)
3.4j

0 and
SyntaxError: invalid syntax
0and 5
0

0.0 and
SyntaxError: invalid syntax
0.00 and 4
0.0

j and 4
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    j and 4
NameError: name 'j' is not defined
0j and 5
0j


{} and ()
{}

{} and {}
{}
() and {}
()

[] and ()
[]




#3.not
not True
False

not 0
True

not {}
True

not[]
True

 
not()
True

noy0.0
SyntaxError: invalid syntax
not 0.0
True
not 0
True
not 0j
True

not ''
True



#or
0 or 5
5

0.0j or 5
5
>>> 
>>> 0.0j or ''
''
>>> 
>>> 0.0j or 'fgh'
'fgh'
>>> 'gfh' or 0.0j
'gfh'
>>> 
>>> 5 or 0
5
>>> 
>>> 5 or 7
5
>>> 
>>> 7 or 5
7
>>> 
>>> 
>>> 
>>> not 90 and 88
False
>>> 
>>> not 90
False
>>> 
>>> 12 and 7 or 45
7
>>> 
>>> 
