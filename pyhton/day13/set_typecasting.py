Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #set
>>> a={12,34,78,'python'}
>>> 
>>> int(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
>>> 
>>> float(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'set'
>>> 
>>> bool(a)
True
>>> 
>>> complex(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    complex(a)
TypeError: complex() argument must be a string or a number, not set
>>> 
>>> str(a)
"{'python', 12, 34, 78}"
>>> 
>>> list()a
SyntaxError: invalid syntax
list(a)
['python', 12, 34, 78]

tuple(a)
('python', 12, 34, 78)

set(a)
{'python', 12, 34, 78}

dict(a)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    dict(a)
ValueError: dictionary update sequence element #0 has length 6; 2 is required
