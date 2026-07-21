Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list-->typecasting

a=[12,34,56]
int(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'list'
>>> bool(a)
True
>>> 
>>> complex(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    complex(a)
TypeError: complex() argument must be a string or a number, not list
>>> 
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    dict(a)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
>>> 
>>> str(a)
'[12, 34, 56]'
>>> 
>>> list(a)
[12, 34, 56]
>>> 
>>> set(a)
{56, 34, 12}
>>> 
>>> tuple(a)
(12, 34, 56)
