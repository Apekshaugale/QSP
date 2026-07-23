Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#division
5/7
0.7142857142857143

5//7
0

5%7
5

(6j)/(5+6j)
(0.5901639344262294+0.4918032786885245j)

(6)/(5+6j)
(0.4918032786885245-0.5901639344262294j)

(6j)/(5)
1.2j
(6j)//(5)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    (6j)//(5)
TypeError: unsupported operand type(s) for //: 'complex' and 'int'
(6j)//(5+6j)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    (6j)//(5+6j)
TypeError: unsupported operand type(s) for //: 'complex' and 'complex'
>>> 
>>> (6j)%(5)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    (6j)%(5)
TypeError: unsupported operand type(s) for %: 'complex' and 'int'
>>> 
>>> 4.6/7
0.6571428571428571
>>> 
>>> 6.7//5.7
1.0
>>> 
>>> 4.6//7
0.0
>>> 4.6%7
4.6
>>> 
>>> 6.7%5.7
1.0
>>> 
>>> 4.6%7
4.6
>>> 
>>> 'hii'/9
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    'hii'/9
TypeError: unsupported operand type(s) for /: 'str' and 'int'
