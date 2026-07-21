Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict
a={'a':'adf','she':'he','shreya':'shree'}

int(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
>>> 
>>> float(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'dict'
>>> 
>>> bool(a)
True
>>> 
>>> complex(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    complex(a)
TypeError: complex() argument must be a string or a number, not dict
>>> 
>>> str(a)
"{'a': 'adf', 'she': 'he', 'shreya': 'shree'}"
>>> 
>>> list(a)
['a', 'she', 'shreya']
>>> 
>>> set(a)
{'she', 'a', 'shreya'}
>>> 
>>> tuple(a)
('a', 'she', 'shreya')
>>> 
>>> dict(a)
{'a': 'adf', 'she': 'he', 'shreya': 'shree'}
