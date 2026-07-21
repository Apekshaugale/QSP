Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Slicing & Indexing Traps
s = "PYTHONPROGRAMMING"
print(s[-5:-10:-1])
MARGO

s = "ABCDEFGHIJK"
print(s[8:2:-2])
IGE

s = "PYTHON"
print(s[::-3])
NT

s = "COMPUTER"
print(s[-1:-9:-2])
RTPO

s = "ABCDEFGHIJ"
print(s[5:1:-1])
FEDC

#Nested List Logic
a = [10,20,[30,40,[50,60]],70]
#7
a[2][2][1]
60

#Replace 50 with 500
a = [10,20,[30,40,[50,60]],70]
a[2][2]
[50, 60]
a[2]
[30, 40, [50, 60]]
a[2][2]
[50, 60]
a[2][2][0]=500
a[2][2]
[500, 60]
#list is mutable
a
[10, 20, [30, 40, [500, 60]], 70]

#
KeyboardInterrupt
#Predict output.
a = [1,2,3]
b = a
c = a[:]
a.append(4)
a
[1, 2, 3, 4]
b
[1, 2, 3, 4]
c
[1, 2, 3]

#Why?
a = [[1,2],[3,4]]
b = a.copy()
#shallow copy
a
[[1, 2], [3, 4]]
b
[[1, 2], [3, 4]]
id(a)
2678634166336
id(b)
2678633495360
id(a[0])
2678597197824
id(b[0])
2678597197824
#id of nested list same in shallow copy
a[0][0] = 100
#if chnage in one nested list will affect the other list because id is same of nested list in shallow copy
a
[[100, 2], [3, 4]]
b
[[100, 2], [3, 4]]
a[1][0] = 100
a
[[100, 2], [100, 4]]
b
[[100, 2], [100, 4]]


a = [[1,2],[3,4]]
b = a[:]
a[1].append(5)
print(b)
[[1, 2], [3, 4, 5]]
a
[[1, 2], [3, 4, 5]]


#Tuple Mystery
t = (10,20,[30,40])
t[2].append(50)
print(t)
(10, 20, [30, 40, 50])
#Why does it work?--->because in tuple we can not make modification but we can modify nested list preset in it.indirectly we can perform modification in tuple.

#Why does it fail?
t = (1,2,[3,4])
t[2] = [5,6]
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    t[2] = [5,6]
TypeError: 'tuple' object does not support item assignment

t = ([1,2],[3,4])
t[0].append(100)
t
([1, 2, 100], [3, 4])


t = (1,2,3)
print(id(t))
2678634199088
t += (4,)
print(id(t))
2678633615408
t
(1, 2, 3, 4)
#Same id or different id? Why?

#Level 4: Dictionary Brain Teasers

#How many key-value pairs remain?
d = {1:"A",True:"B",1.0:"C"}
print(d)
{1: 'C'}
#true=1.so it takes updated value.

d = {}
d[(1,2)] = "tuple"
d[(1,2,3)] = "python"
d
{(1, 2): 'tuple', (1, 2, 3): 'python'}
print(len(d))
2
>>> #we use composite key
>>> 
>>> 
>>> d = {}
>>> d["name"] = "Alex"
>>> print(d)
{'name': 'Alex'}
>>> d["name"] = "John"
>>> print(d)
{'name': 'John'}
>>> 
>>> d = {"x":10}
>>> print("x" in d)
True
>>> print(10 in d)
False
>>> #always key layer is visible
>>> 
>>> 
>>> d = {"a":1}
>>> print(d.get("b"))
None
>>> print(d["b"])
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    print(d["b"])
KeyError: 'b'
>>> 
