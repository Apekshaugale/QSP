Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #subtraction
>>> 5-6
-1
>>> 
>>> 6.8-9.0
-2.2
>>> 
>>> true-false
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    true-false
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> 
>>> True-False
1
>>> 
>>> 'string'-'list'
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    'string'-'list'
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> 
>>> (2+6j)-(5+5j)
(-3+1j)
>>> 
>>> (2+6j)-8
(-6+6j)
>>> 
>>> (2+6j)-'she'
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    (2+6j)-'she'
TypeError: unsupported operand type(s) for -: 'complex' and 'str'

'she'-'hi'
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    'she'-'hi'
TypeError: unsupported operand type(s) for -: 'str' and 'str'

[1,2,3]-[4,5,6]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    [1,2,3]-[4,5,6]
TypeError: unsupported operand type(s) for -: 'list' and 'list'

{3,4,6}-{5,7,8}
{3, 4, 6}


#in set subtraction out is uncommon element from first set.

(2,3)-(4,)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    (2,3)-(4,)
TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'
