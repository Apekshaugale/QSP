Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='python'
s.reverse()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s.reverse()
AttributeError: 'str' object has no attribute 'reverse'
list(s)
['p', 'y', 't', 'h', 'o', 'n']
s
'python'
s=list(s)
s
['p', 'y', 't', 'h', 'o', 'n']
s.reverse()
s
['n', 'o', 'h', 't', 'y', 'p']
str(s)
"['n', 'o', 'h', 't', 'y', 'p']"
s.split()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s.split()
AttributeError: 'list' object has no attribute 'split'
s
['n', 'o', 'h', 't', 'y', 'p']
s=str(s)
s
"['n', 'o', 'h', 't', 'y', 'p']"
s.split()
["['n',", "'o',", "'h',", "'t',", "'y',", "'p']"]
s='python'
s.replace('onthyp','python')
'python'
s
'python'
s.replace('python','onthyp')
'onthyp'


#1. Reverse Without [::-1]
s = "PYTHON"
s.replace("PYTHON",'NOHTYP')
'NOHTYP'

#2. Character Frequency
s = "programming"
s.count('p')
1
s.count('r')
2
s.count('0')
0
s.count('o')
1
s.count('g')
2
s.count('r')
2
s.count('a')
1
s.count('m')
2
s.count('i')
1
s.count('n')
1

s = "Python"
print(s.index("z"))
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print(s.index("z"))
ValueError: substring not found

s = "Python"
print(s.find("z"))
-1

s = "Python"
print(s[10])
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print(s[10])
IndexError: string index out of range

s = "Python"
s[0] = "J"
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    s[0] = "J"
TypeError: 'str' object does not support item assignment


s = "hello123"
print(s.isalpha())
False

#List Methods + Errors
a = [10,20,30]
a.remove(50)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a.remove(50)
ValueError: list.remove(x): x not in list

a = [10,20,30]
print(a.pop(5))
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    print(a.pop(5))
IndexError: pop index out of range
print(a.index(100))
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    print(a.index(100))
ValueError: list.index(x): x not in list

a = [1,2,3]
a.append(4,5)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a.append(4,5)
TypeError: list.append() takes exactly one argument (2 given)

a = [1,2,3]
a.extend(100)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a.extend(100)
TypeError: 'int' object is not iterable

#Tuple Methods + Errors
t = (10,20,30)
print(t.index(50))
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    print(t.index(50))
ValueError: tuple.index(x): x not in tuple

t = (10,20,30)
t.append(40)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    t.append(40)
AttributeError: 'tuple' object has no attribute 'append'

t = (10,20,30)
t[0] = 100
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    t[0] = 100
TypeError: 'tuple' object does not support item assignment

t = (10,20,30)
print(t.count(10))
1

#Set Methods + Errors
s = {1,2,3}
s.remove(10)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    s.remove(10)
KeyError: 10

s = {1,2,3}
s.discard(10)
s
{1, 2, 3}

s = {1,2,3}
print(s.pop(1))
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    print(s.pop(1))
TypeError: set.pop() takes no arguments (1 given)

s = {1,2,3}
s.add([4,5])
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    s.add([4,5])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')

s = {1,2,3}
s.update(4)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    s.update(4)
TypeError: 'int' object is not iterable

#Dictionary Methods + Errors
d = {"a":10}
print(d["b"])
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    print(d["b"])
KeyError: 'b'

d = {"a":10}
print(d.get("b"))
None

d = {"a":10}
d["a"] = 20
print(d)
{'a': 20}

d = {"a":10}
d.update({"b":20})
print(d)
{'a': 10, 'b': 20}

d = {[1,2]:100}
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    d = {[1,2]:100}
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')

#Type Conversion + Errors
int("123")
123

int("12.5")
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    int("12.5")
ValueError: invalid literal for int() with base 10: '12.5'

int(1+2j)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    int(1+2j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

float("abc")
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    float("abc")
ValueError: could not convert string to float: 'abc'

list(100)
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    list(100)
TypeError: 'int' object is not iterable

set(100)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    set(100)
TypeError: 'int' object is not iterable

print(bool(""))
False

#because no spacing

print(bool(" "))
True

print(bool("False"))
True

print(bool([]))
False

print(bool([0]))
True

help(keywords)
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    help(keywords)
NameError: name 'keywords' is not defined
help('keywords')

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> import keyword
>>> keyword.iskeyword('id')
False
>>> a
[1, 2, 3]
>>> a={2:3}
>>> a.popitem(3)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    a.popitem(3)
TypeError: dict.popitem() takes no arguments (1 given)
