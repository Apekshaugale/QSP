Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#individual data type
#there are four types:
#integer
#flaot
#complex
#bool
a=2
print(bool(a))
True


#2.float-->it is a real number with decimal point in it.
#float values can be both +ve and _ve value.
#ranfe is -infinity to +infinity


#typecasting
int
<class 'int'>
#int

a=10
float(a)
10.0
int(a)
10

str(a)
'10'

complex(a)
(10+0j)
bool(a)
True
tuple(a)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable

















#float
#a=10.45
float(a)
10.0
str(a)
'10'
int(a)
10
complex(a)
(10+0j)
float(a)
10.0
tuple(a)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
bool(a)
True
list()a
SyntaxError: invalid syntax
list(a)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable


#bool DT
a=True
float(a)
1.0
int(a)
1
bool(a)
True
complex(a)
(1+0j)
str(a)
'True'
tuple(a)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    tuple(a)
TypeError: 'bool' object is not iterable
list(a)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    list(a)
TypeError: 'bool' object is not iterable
)
SyntaxError: unmatched ')'
set(a)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    set(a)
TypeError: 'bool' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    dict(a)
TypeError: 'bool' object is not iterable


#complex
a=3i+2j
SyntaxError: invalid decimal literal
>>> a=3+2j
>>> float(a)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> int(a)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> float(a)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> bool(a)
True
>>> complex(a)
(3+2j)
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    set(a)
TypeError: 'complex' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    dict(a)
TypeError: 'complex' object is not iterable
