Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#addition
(1,2,3)+{3}
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    (1,2,3)+{3}
TypeError: can only concatenate tuple (not "set") to tuple

(1,2,3)+(3)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    (1,2,3)+(3)
TypeError: can only concatenate tuple (not "int") to tuple
(1,2,3)+(3,)
(1, 2, 3, 3)
#in tuple comma is mainditory

{23,45}+{5,5}
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    {23,45}+{5,5}
TypeError: unsupported operand type(s) for +: 'set' and 'set'

(1+3j)+(3j)
(1+6j)
>>> 
>>> 2.3+5
7.3
>>> 
>>> (1+3j)+5
(6+3j)
>>> 
>>> True+1
2
>>> 
>>> True+5
6
>>> 
>>> False+(5+5j)
(5+5j)
>>> 
>>> 'hello'+'shree'
'helloshree'
>>> 
>>> 'hello'+(5j)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    'hello'+(5j)
TypeError: can only concatenate str (not "complex") to str
>>> 
>>> [4,5]+[6,7]
[4, 5, 6, 7]
>>> (1,3,4)+(4,6,7)
(1, 3, 4, 4, 6, 7)
