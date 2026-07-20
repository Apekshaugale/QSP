Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> x=(1,2,3,[1,2,3])
>>> x[3]
[1, 2, 3]
>>> x[3][1]=4
>>> x
(1, 2, 3, [1, 4, 3])
>>> x=(1,2,3,4)
>>> x[2]
3
>>> x[2]=6
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x[2]=6
TypeError: 'tuple' object does not support item assignment
