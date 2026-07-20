Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
len(str([5,6,7]))
9
a='good morning'
a[8:3]
''
isinstance((12),(float,complex,tuple))
False
d={'name':'alexander'}
len(d['name'])
9
a = "Python"
print(a[-10:])
Python
print("python".index("z"))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print("python".index("z"))
ValueError: substring not found
print("python".find("z"))
-1
print(bool(" "))
True
print("abc123".isalpha())
False
print("123abc".isdigit())
False
print("Python"[::-2])
nhy
print("Hello".replace("z","x"))
Hello
#if specified character is not peresent then it will give as output
print(len(" "))
1
print("Python"[100])
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print("Python"[100])
IndexError: string index out of range
#because 100 is not present at index postion

#List-Based Thinking Questions
a=[10,20,30]
print(a.pop())#vn.pop(position)
30
#by default it will remove lst element
a
[10, 20]

a=[1,2,3]
a.append([4,5])#vn.append(element)
a
[1, 2, 3, [4, 5]]
#it will add element at last but with boundary conditions

a=[1,2,3]
a.extend([4,5])
#vn.extend(element),it will add element wthout boundary condition
a
[1, 2, 3, 4, 5]
#in extend we can use only immutable data type.

a=[1,2,3]
a.remove(10)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.remove(10)
ValueError: list.remove(x): x not in list

a=[]
print(bool(a))
False

a=[1,2,3]
print(a[5:])
[]

a=[1,2,3]
print(a[::-1])
[3, 2, 1]

a=[1,2,2,2,3]
print(a.count(2))
3

a=[10,20]
b=a
b.append(30)
a
[10, 20, 30]
b
[10, 20, 30]
#if we make chnage in one affect another set because id of both is same

a=[1,2,3]
print(id(a)==id(a))
True

#Tuple-Based Thinking Questions
t=(10)
print(type(t))
<class 'int'>

t=('10')
print(type(t))
<class 'str'>

#in tuple comma ia manditory
t=('10',)
print(type(t))
<class 'tuple'>

KeyboardInterrupt
t=(1,2,3)
t[0]=100
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    t[0]=100
TypeError: 'tuple' object does not support item assignment
#tuple ois immutable

t=(1,2,[3,4])
t[2].append(5)
t
(1, 2, [3, 4, 5])

t=(1,2,3)
print(t.index(10))
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    print(t.index(10))
ValueError: tuple.index(x): x not in tuple


#Set-Based Thinking Questions
s={1,2,3}
s.add(2)
s
{1, 2, 3}

s={1,2,3}
s.remove(5)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    s.remove(5)
KeyError: 5

s={1,2,3}
s.discard(5)
s
{1, 2, 3}

KeyboardInterrupt
KeyboardInterrupt
s={1,2,3}
C
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
print(s.pop())
1
s
{2, 3}
print(s[0])
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    print(s[0])
TypeError: 'set' object is not subscriptable
#set is unordered data type

s={1,2,2,2,3}
print(len(s))
3
s={[1,2]}
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    s={[1,2]}
TypeError: cannot use 'list' as a set element (unhashable type: 'list')

s={(1,2)}
print(type(next(iter(s))))
<class 'tuple'>

print(hash("python"))
7535933630233993118

#Dictionary-Based Thinking Questions
d={"a":10,"b":20}
print(d["c"])
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    print(d["c"])
KeyError: 'c'

d={"a":10}
print(d.get("b"))
None

d={1:"one",1:"python"}
print(d)
{1: 'python'}
#latest updated value

d={(1,2):"A"}
print(d[(1,2)])
A
#composite key

d={[1,2]:"A"}
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    d={[1,2]:"A"}
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')

#in part  of we can use only tuples not list

d={"x":10}
for i in d:
     print(i)

     
x

d={"x":10}
print(len(d))
1

KeyboardInterrupt
d={"a":10}
d.update({"b":20})
d
{'a': 10, 'b': 20}

d={"a":10}
print(bool(d))
True

d={}
print(bool(d))
False

#Interview-Level Tricky Questions
print(bool("False"))
True

print(bool("0"))
True

#internally False =0 and True=1

a=12.5
print(complex(a))
(12.5+0j)

print(isinstance(True,int))
True

print(id(250)==id(250))
True

print(id(258)==id(258))
True


#
KeyboardInterrupt
#Challenge Mode
a=[1,2,3]
print(str(a))
[1, 2, 3]
print(len(str(a)))
9
#( [ 1 , 2,3 ] )
>>> 
>>> print(round(12.5))
12
>>> 
>>> print(round(13.5))
14
>>> 
>>> print(round(14.5))
14
>>> 
>>> 
>>> print(bool(""))
False
>>> 
>>> print(bool(" "))
True
>>> 
>>> print(bool("0"))
True
>>> 
>>> print(bool(0))
False
>>> 
>>> s={1,2,3}
>>> print(s.pop())
1
>>> 
>>> d={"name":"Alexander"}
>>> print(len(d["name"]))
9
