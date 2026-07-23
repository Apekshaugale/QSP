Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#operator task
print(2 ** 4)
16

a = 10
b = 0
a/b
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a/b
ZeroDivisionError: division by zero

print("10" + "20")
1020

print("10" - "20")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print("10" - "20")
TypeError: unsupported operand type(s) for -: 'str' and 'str'

print(10 > 5)
True

print(10 < 5)
False

print(10 == "10")
False

print(10 != 20)
True

lst = [10, 20, 30]
print(lst[5])
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(lst[5])
IndexError: list index out of range

s = "Python"
print(s[10])
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(s[10])
IndexError: string index out of range

lst = [1, 2, 3]
lst.remove(5)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    lst.remove(5)
ValueError: list.remove(x): x not in list

lst = [10, 20, 30]
print(lst.index(50))
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(lst.index(50))
ValueError: list.index(x): x not in list

d = {"name": "Apeksha"}
print(d["age"])
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(d["age"])
KeyError: 'age'

print(age)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(age)
NameError: name 'age' is not defined

print("10" + 20)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print("10" + 20)
TypeError: can only concatenate str (not "int") to str

len(100)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    len(100)
TypeError: object of type 'int' has no len()

import maths
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    import maths
ModuleNotFoundError: No module named 'maths'

int("Python")
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    int("Python")
ValueError: invalid literal for int() with base 10: 'Python'


s = "Python"
s[0] = "J"
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s[0] = "J"
TypeError: 'str' object does not support item assignment

t = (10, 20, 30)
t[1] = 100
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    t[1] = 100
TypeError: 'tuple' object does not support item assignment

a = {1, 2, 3}
print(a[0])
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print(a[0])
TypeError: 'set' object is not subscriptable

d = {"a": 10}
print(d["b"])
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    print(d["b"])
KeyError: 'b'

lst = [1, 2, 3]
print(lst[1.5])
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    print(lst[1.5])
TypeError: list indices must be integers or slices, not float
>>> 
>>> a = [10, 20, 30]
>>> print(a.pop(5))
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    print(a.pop(5))
IndexError: pop index out of range
>>> 
>>> a = {1, 2, 3}
>>> a.remove(5)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a.remove(5)
KeyError: 5
>>> 
>>> a = {1, 2, 3}
>>> a.discard(5)
>>> print(a)
{1, 2, 3}
>>> 
>>> d = {"x": 10}
>>> print(d.get("y"))
None
>>> 
>>> s = "123"
>>> print(int(s))
123
>>> 
