Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list
#in list data type we can do imdexing and slicing
#each element seperated by comma
#list datatype is orderded data type
#in list data type we can do imdexing and slicing
e=[100,89.34,True,'welcome','walmart','goodluck',12]
e[6]
12
e[100]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    e[100]
IndexError: list index out of range
e[2]
True
e[3][2:4:1]
'lc'
e[3]=100
e
[100, 89.34, True, 100, 'walmart', 'goodluck', 12]

e[2]
True
e[2]=False
e
[100, 89.34, False, 100, 'walmart', 'goodluck', 12]
e[2][1]=@
SyntaxError: invalid syntax
dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'e']
dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
#adding element into the list
 #adding,append,insert
#append()
#syntax-->vn.append(element)
x=[]
x
[]
x.append(10)#fisrt we will add single value datatype
x
[10]
x.append(45.23)
x
[10, 45.23]
x.append(1+2j)
x
[10, 45.23, (1+2j)]
x.append(True)
x
[10, 45.23, (1+2j), True]
x.append('Python')#second part we will addcollection data type
x
[10, 45.23, (1+2j), True, 'Python']
x.append((23,900))
x
[10, 45.23, (1+2j), True, 'Python', (23, 900)]
x.append([12,13,14])
x
[10, 45.23, (1+2j), True, 'Python', (23, 900), [12, 13, 14]]
x.append({500,699})
x
[10, 45.23, (1+2j), True, 'Python', (23, 900), [12, 13, 14], {699, 500}]
#set is unoredred datatype
x.append({500:699})
x
[10, 45.23, (1+2j), True, 'Python', (23, 900), [12, 13, 14], {699, 500}, {500: 699}]
#in append methods-->error
a.append()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a.append()
NameError: name 'a' is not defined
x.append()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    x.append()
TypeError: list.append() takes exactly one argument (0 given)
x.append(12,2)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    x.append(12,2)
TypeError: list.append() takes exactly one argument (2 given)
#i want to aviod this error noe use tuple
x.append((12,2))
x
[10, 45.23, (1+2j), True, 'Python', (23, 900), [12, 13, 14], {699, 500}, {500: 699}, (12, 2)]
#in the given list if you want to add any element you can add using append methods
#it will add at the end of list



#2.extend()
#syntax-->vn.extend(iterable)iterable mens collection datatype means only we hvae to pass string ,tuple,list.if we pass single value it show error
a.append([100,200,300])
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a.append([100,200,300])
NameError: name 'a' is not defined
a[]
SyntaxError: invalid syntax
a()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a()
NameError: name 'a' is not defined
a
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a
NameError: name 'a' is not defined
a=[]
a
[]
a.append([100,200,300])
a
[[100, 200, 300]]
a.extend((200,300))
a
[[100, 200, 300], 200, 300]
a.extend([100,200,300])
a
[[100, 200, 300], 200, 300, 100, 200, 300]
a.extend({200:798})
a
[[100, 200, 300], 200, 300, 100, 200, 300, 200]
a
[[100, 200, 300], 200, 300, 100, 200, 300, 200]
a.extend({200:798})
a
[[100, 200, 300], 200, 300, 100, 200, 300, 200, 200]
a.extend(('pyhton'))
a
[[100, 200, 300], 200, 300, 100, 200, 300, 200, 200, 'p', 'y', 'h', 't', 'o', 'n']
a.extend({587:787})
a
[[100, 200, 300], 200, 300, 100, 200, 300, 200, 200, 'p', 'y', 'h', 't', 'o', 'n', 587]
a.append({587:787})
a
[[100, 200, 300], 200, 300, 100, 200, 300, 200, 200, 'p', 'y', 'h', 't', 'o', 'n', 587, {587: 787}]
a.extend('hello')
a
[[100, 200, 300], 200, 300, 100, 200, 300, 200, 200, 'p', 'y', 'h', 't', 'o', 'n', 587, {587: 787}, 'h', 'e', 'l', 'l', 'o']
a.append('hello')
a
[[100, 200, 300], 200, 300, 100, 200, 300, 200, 200, 'p', 'y', 'h', 't', 'o', 'n', 587, {587: 787}, 'h', 'e', 'l', 'l', 'o', 'hello']
len(a)
22
z.append()
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    z.append()
NameError: name 'z' is not defined
a.append()
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    a.append()
TypeError: list.append() takes exactly one argument (0 given)
a.append(200)

a.entend(200)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    a.entend(200)
AttributeError: 'list' object has no attribute 'entend'. Did you mean: 'extend'?
a
[[100, 200, 300], 200, 300, 100, 200, 300, 200, 200, 'p', 'y', 'h', 't', 'o', 'n', 587, {587: 787}, 'h', 'e', 'l', 'l', 'o', 'hello', 200]


#insert()
#syntax
#-->vn.insert(position,value)
s=[1,2,3,4]

s.insert(0,100)
s
[100, 1, 2, 3, 4]
s.insert(4,"pyhton")
s
[100, 1, 2, 3, 'pyhton', 4]
s.insert(2,[1,2,3])
s
[100, 1, [1, 2, 3], 2, 3, 'pyhton', 4]
s.insert(6,True)
s
[100, 1, [1, 2, 3], 2, 3, 'pyhton', True, 4]
#if the specified position is not present that element will added at last not error
s.insert(60,'morning')
s.insert(-9,'morning')
s
['morning', 100, 1, [1, 2, 3], 2, 3, 'pyhton', True, 4, 'morning']
s.insert(-20,'Apeksha')
s
['Apeksha', 'morning', 100, 1, [1, 2, 3], 2, 3, 'pyhton', True, 4, 'morning']


#how to remove element from list --->pop,remove,clear,(keyword)del var_nam
#pop()
#syntax-->vn.pop()
#vn.pop(position)
s
['Apeksha', 'morning', 100, 1, [1, 2, 3], 2, 3, 'pyhton', True, 4, 'morning']
s.pop()
'morning'

s.pop(4)
[1, 2, 3]
s
['Apeksha', 'morning', 100, 1, 2, 3, 'pyhton', True, 4]
#by the help of position if you want to delete element you can use pop method.
s.pop(0)
'Apeksha'
s
['morning', 100, 1, 2, 3, 'pyhton', True, 4]


#remove()
#syntax-->vn.remove(element)

x=[1,2,3,4,5,[90,100,200],'hello',89.59]
x
[1, 2, 3, 4, 5, [90, 100, 200], 'hello', 89.59]
x[5]
[90, 100, 200]
x[5].pop(1)
100
x
[1, 2, 3, 4, 5, [90, 200], 'hello', 89.59]

x[5].clear
<built-in method clear of list object at 0x000001B5CA016180>
x[5].clear()
x
[1, 2, 3, 4, 5, [], 'hello', 89.59]
del x[5]
x
[1, 2, 3, 4, 5, 'hello', 89.59]


r=[[[100,300,600],900,1000]]
r
[[[100, 300, 600], 900, 1000]]
r[0]
[[100, 300, 600], 900, 1000]
r[0][0]
[100, 300, 600]
r[0][0].pop(1)
300
r
[[[100, 600], 900, 1000]]
#same you can do this using remove method


#count--->var-name.count(element)

r.count(100)
0
r.count(1000)
0

>>> #index--->var_nam.index(element,si,ei+1)
>>> d=[100,200,300,400,100,500,200]
>>> d.index(100)
0
>>> d.index(100,2)
4
>>> d.index(200,2)
6
>>> d.index(200,1)
1
>>> d.index(200,4)
6
>>> 
>>> 
>>> #reverse()
>>> d
[100, 200, 300, 400, 100, 500, 200]
>>> d[::-1]
[200, 500, 100, 400, 300, 200, 100]
>>> 
>>> 

... 
>>> 

... 
>>> 

>>> d.reverse()
>>> d
[200, 500, 100, 400, 300, 200, 100]
