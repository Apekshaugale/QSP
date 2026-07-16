Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#set
#add-->vn.add(element)
#update-->vn.update(iterable)
#pop-->vn.pop()
#remove--->vn.remove(element)
#discard--->vn.discard(element)
#clear-->vn.clear()
#del vn
#intersection--->vn1.intersection(vn2)
#symmetric_difference--->vn1.symmetric_difference(vn2)
#difference--->vn1.difference(vn2)
#isdisjoint-->vn1.isdisjoint(vn2)
#issuperset-->vn1.issuperset(vn2)
#issubset-->vn1.issubset(vn2)
#copy--->new vn=original vn
#union--->vn1.union(vn2)
#intersection_update--->vn1.intersection_update(vn2)

x={10,'a','b',56,55,100}
y={10,'a','b',66,992,100}
y.intersection(y)
{992, 'b', 66, 100, 10, 'a'}
#output is blankscape
#when you call x we will the output as updated data not original data
y.intersection_update(y)

y
{992, 'b', 66, 100, 10, 'a'}
y.intersection_update(x)


y

y
{'b', 10, 100, 'a'}
x
{'b', 100, 55, 56, 10, 'a'}
x.intersection_update(y)

x
{'b', 10, 100, 'a'}
y.intersection_update(x)

y
{'b', 10, 100, 'a'}
x
{'b', 10, 100, 'a'}
x.symmetric_difference(y)
set()
x={10,'a','b',56,55,100}
y={10,'a','b',66,992,100}
y.intersection_update(x)

y
{'b', 10, 100, 'a'}
x
{'b', 100, 55, 56, 10, 'a'}


#symmetric_difference--->vn1.symmetric_difference(vn2)
#symmetric_difference_update--->vn1.symmetric_difference_update(vn2)
#we get balnk space output
#if you call variable(original)you get uncommon element and always get updated data
e={1,2,'python','java','sql'}
e={1,2,'python',11,12,900,111,'sql'}
f={1,2,'python',11,12,900,111,'sql'}
e
{1, 2, 900, 11, 12, 'python', 111, 'sql'}
f
{1, 2, 900, 11, 12, 'python', 111, 'sql'}
e={1,2,'python','java','sql'}
e
{1, 2, 'java', 'sql', 'python'}
f
{1, 2, 900, 11, 12, 'python', 111, 'sql'}
r.symmetric_difference(f)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    r.symmetric_difference(f)
NameError: name 'r' is not defined
e.symmetric_difference(f)
{900, 'java', 11, 12, 111}
e
{1, 2, 'java', 'sql', 'python'}
f
{1, 2, 900, 11, 12, 'python', 111, 'sql'}
e.symmetric_difference_update(f)

e
{900, 'java', 11, 12, 111}
f
{1, 2, 900, 11, 12, 'python', 111, 'sql'}
f.symmetric_difference_update(e)
f
{1, 2, 'java', 'python', 'sql'}
e
{900, 'java', 11, 12, 111}
e.symmetric_difference_update(f)

e
{1, 2, 900, 11, 12, 111, 'python', 'sql'}
f
{1, 2, 'java', 'python', 'sql'}
e.symmetric_difference_update(f)

e
{900, 'java', 11, 12, 111}
f
{1, 2, 'java', 'python', 'sql'}
e.symmetric_difference_update(f)

e
{1, 2, 900, 11, 12, 111, 'python', 'sql'}
f
{1, 2, 'java', 'python', 'sql'}
e.symmetric_difference_update(f)

e
{900, 'java', 11, 12, 111}
f
{1, 2, 'java', 'python', 'sql'}
f.symmetric_difference_update(e)

f
{1, 2, 900, 11, 12, 'python', 111, 'sql'}
e
{900, 'java', 11, 12, 111}


#intersection and symmetric difference
d={'morning','evening','hii','bye','hello','snap'}
e={'hii','good','wlmart','insta','bad','snap','hello'}
d.intersection(e)
{'hello', 'hii', 'snap'}
e.intersection(d)
{'hello', 'hii', 'snap'}
d
{'morning', 'evening', 'hello', 'hii', 'bye', 'snap'}
e
{'insta', 'good', 'wlmart', 'hello', 'hii', 'bad', 'snap'}
d.intersection_update(e)

d
{'hello', 'hii', 'snap'}
e
{'insta', 'good', 'wlmart', 'hello', 'hii', 'bad', 'snap'}
e.intersection_update(d)

e
{'hello', 'hii', 'snap'}
d
{'hello', 'hii', 'snap'}
#intersection--->common element
d={'morning','evening','hii','bye','hello','snap'}
e={'hii','good','wlmart','insta','bad','snap','hello'}
d.symmetric_difference(e)
{'wlmart', 'good', 'morning', 'bye', 'insta', 'evening', 'bad'}
e.symmetric_difference(d)
{'wlmart', 'good', 'morning', 'bye', 'insta', 'evening', 'bad'}
e.symmetric_difference_update(d)

e
{'wlmart', 'good', 'morning', 'bye', 'insta', 'evening', 'bad'}
e
{'wlmart', 'good', 'morning', 'bye', 'insta', 'evening', 'bad'}
f
{1, 2, 900, 11, 12, 'python', 111, 'sql'}
d
{'morning', 'evening', 'hello', 'hii', 'bye', 'snap'}
e
{'wlmart', 'good', 'morning', 'bye', 'insta', 'evening', 'bad'}
d.symmetric_difference_update(e)

d
{'hii', 'insta', 'wlmart', 'hello', 'good', 'bad', 'snap'}
e
{'wlmart', 'good', 'morning', 'bye', 'insta', 'evening', 'bad'}


#difference()
a={1000,2000,3000,4000}
b={4000,5000,1000,2000}
a.difference(b)
{3000}
a
{4000, 1000, 3000, 2000}
b
{5000, 1000, 4000, 2000}
b.difference(a)
{5000}
a
{4000, 1000, 3000, 2000}
b
{5000, 1000, 4000, 2000}
#difference update()
a.difference_update(b)

a
{3000}
b
{5000, 1000, 4000, 2000}
a.difference_update(b)

a
{3000}
b
{5000, 1000, 4000, 2000}
b.difference_update(a)

b
{5000, 1000, 4000, 2000}
>>> a
{3000}
>>> {3000}
{3000}
>>> dir(set)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> 
>>> 
>>> type()
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    type()
TypeError: type() takes 1 or 3 arguments
>>> type(b)
<class 'set'>
>>> id(b)
2121962841568
>>> round(d)
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    round(d)
TypeError: type set doesn't define __round__ method
>>> a=2
>>> round(a)
2
a=2.3
round(a)
2
a=2.5
round(a)
2
a=2.6
a
2.6
round(a)
3
#if number is even and decimal is less that 5 it will won't add .it it greater than 6or greter then upadte value
max(a)
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    max(a)
TypeError: 'float' object is not iterable
min()
Traceback (most recent call last):
  File "<pyshell#167>", line 1, in <module>
    min()
TypeError: min expected at least 1 argument, got 0
