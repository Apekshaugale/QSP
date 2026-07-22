Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#relational operator
#which is used to compare between two or more operator
#there are 6 operator
#1.
#1.(==)
#2.(!=)
#3.(>)
#4.(<)
#5.(>=)

#6.(<=)

#1.(==)
#Relational equal to(==)
#it will compare between operands and gives the result as TRUE only if both the ooperand are same.
#syntax-->op1==op2.
#Realtional equal to operator is aslo known as comparision operation.
10==10
True

12==10
False

'abe'=='ABE'
False

10=='halk'
False

#2.relational not equal to(!=)
#It is used to compare 2operator and gives the result as true only if both operands asre differend (not same)
#syntax-->op1!=op2
50!=20
True

50!=50
False

#2.relational greater(>)
#It is used to compare two operand
##syntax-->op1>op2
#complex value can not be campared.
#In string it compare using ASCII value number
#A-Z='65'to'90'
#a-z='97'to'122'
#0-9='48'to'57'

'string'>'abc'
True

'abc'>'cef'
False

'manoj'>'manju'
True

True>False
True
10.5>5.6
True


#4.relational lesser than (>)
#2.relational greater than(>) is not support to dictinary and complex data type.
#It will give result True only if op1 is greater than op2.
#to find ASCII vslue we want  required ord().
#ord()-->it is a inbuild function used to give ASCII vlalue for particular char
#suntax-->ord('char')

{2,3,4}>{4,4,5}
False

{3:34}>{2:4}
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    {3:34}>{2:4}
TypeError: '>' not supported between instances of 'dict' and 'dict'

(2+3j)>(3+3j)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    (2+3j)>(3+3j)
TypeError: '>' not supported between instances of 'complex' and 'complex'

'string'>'gij'
True


#4.relational lesser than (<)
#.relational lesser than(>) is used two compare two operand .it give s result True if only one operand is lesser tan other.
##syntax-->op1<op2
'string'<'bdf'
False

[2,34,5]<[5,56,4]
True

{2:3}<{3:4}
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    {2:3}<{3:4}
TypeError: '<' not supported between instances of 'dict' and 'dict'
{2,2,4}<{3,4,4}
False

(45,66)<(67,77)
True

#dict,compelx will not support we get error.
(3+3J)<(2+4J)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    (3+3J)<(2+4J)
TypeError: '<' not supported between instances of 'complex' and 'complex'


#4.relational greater than or equal to(>=)
##syntax-->op1>=op2

'string'>='bdf'
True
[2,34,5]>=[5,56,4]
False

{2,2,4}>={3,4,4}
False

(3+3J)>=(2+4J)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    (3+3J)>=(2+4J)
TypeError: '>=' not supported between instances of 'complex' and 'complex'

{2:2,4:5}>={3:4,4:6}
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    {2:2,4:5}>={3:4,4:6}
TypeError: '>=' not supported between instances of 'dict' and 'dict'

[50,60,89]>=[50,60,90]
False

[50,60,90]>=[50,60,89]
True


59>=50
True

'ab'>='df'
False

#6.relational lesser than or equal to(<=)
##syntax-->op1<=op2
#it uses ASCII value to compare twon string
[59,909]<=[40]
False
>>> 
>>> [59,909]<=[40,1000]
False
>>> [39,909]<=[40,1000]
True
>>> 
>>> (1,2,3)<=(4,45)
True
>>> 
>>> {2,3,4}<={9,5,7}
False
>>> 
>>> 5<=6
True
>>> 9<=2
False
>>> 
>>> (2i+3j)<=(3i+4j)
SyntaxError: invalid decimal literal
>>> (2+3j)<=(3+4j)
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    (2+3j)<=(3+4j)
TypeError: '<=' not supported between instances of 'complex' and 'complex'
>>> {2:3,4:4}<={9:5,7:8}
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    {2:3,4:4}<={9:5,7:8}
TypeError: '<=' not supported between instances of 'dict' and 'dict'
