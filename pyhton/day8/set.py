Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
[op
 ;';ihip
 
SyntaxError: unterminated string literal (detected at line 2)
#set()
 
#set data type is unique data type.
 
#set data type is unordered data type .
 
#set data type is mutable data type
 
#set data type is mutable data type.
 
#set dta type it will accept only immutable data type + simgle value data type.
 
#syntax-->vn={ele 1,ele2,ele3,ele4,.....}
 
#set data type is not represented normally we can repesnt it using object only
 
#set()
 

#immutable-->string,tuple.
 
#single value data-->int ,float,bool,complex.
 
a={}
 
type(a)
 
<class 'dict'>
set()
 
set()
e=set()
 
a
 
{}
type(e)
 
<class 'set'>
a={1,2}
 
type(a)
 
<class 'set'>
e={1,23.4,3+5j,False,'hi'}
 
e
 
{False, 1, (3+5j), 23.4, 'hi'}
b={False, 1, (3+5j), 23.4, 'hi',[1,2,3]}
 
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    b={False, 1, (3+5j), 23.4, 'hi',[1,2,3]}
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
b={False, 1, (3+5j), 23.4, 'hi',(1,2,3)}
 
type(b)
 
<class 'set'>
b={False, 1, (3+5j), 23.4, 'hi',{1:2}}
 
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    b={False, 1, (3+5j), 23.4, 'hi',{1:2}}
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
len(b)
 
6
b
 
{False, 1, (3+5j), 23.4, (1, 2, 3), 'hi'}
#false-->0
 
#true-->0
 
e={}
 
e={0,False,True,1,}
 
len(e)
 
2
e={0,False,True,1,1,5,3,2}
 
len(e)
 
5


#methods
 
dir(set)
 
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
#adddding element into set
 
#1.add
 
#2.update method
 
a={}
 
a.add(9)
 
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a.add(9)
AttributeError: 'dict' object has no attribute 'add'
b={1}
 
type(b)
 
<class 'set'>
b.add('False')
 
b
 
{1, 'False'}
b.add(3+3j)
 
b
 
{1, (3+3j), 'False'}
b.add(60)
 
b
 
{1, (3+3j), 60, 'False'}
b.add(3+3j)
 
b
 
{1, (3+3j), 60, 'False'}
#it will not take duplicate value
 
b.add(3+3j)
 
b
 
{1, (3+3j), 60, 'False'}
b.add('hii')
 
b
 
{1, 'False', 'hii', (3+3j), 60}
b.add((1,2,3))
 
b
 
{1, 'False', 'hii', (1, 2, 3), (3+3j), 60}
b.add('abs','a')
 
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    b.add('abs','a')
TypeError: set.add() takes exactly one argument (2 given)
b.add(('abs','a'))
 
b
 
{1, 'False', 'hii', (1, 2, 3), (3+3j), ('abs', 'a'), 60}
#to add multiple element we can't add directly it shows error .we can add using ()
 


#update()
 
#syntax-->vn.update(iterable)
 
x={1}
 
x.update(100)
 
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    x.update(100)
TypeError: 'int' object is not iterable
x.update(1.2)
 
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    x.update(1.2)
TypeError: 'float' object is not iterable
x.update(8+3j)
 
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    x.update(8+3j)
TypeError: 'complex' object is not iterable
x.update((8+3j))
 
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    x.update((8+3j))
TypeError: 'complex' object is not iterable
x.update('python')
 
x
 
{1, 'p', 'h', 'y', 'o', 'n', 't'}
x.update([100,200,300])
 
x
 
{1, 100, 'p', 'h', 'y', 'o', 200, 300, 'n', 't'}
x.update([['a','D']])
 
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    x.update([['a','D']])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
x.update([['a','D'])
         
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
x.update(['a','D'])
         
x
         
{1, 'a', 'D', 100, 'p', 'h', 'y', 'o', 200, 300, 'n', 't'}


#for deleting methods are
         
#1.pop()
         
#2.remove()
         
#3.clear()
         
#dicard()
         
#5.de vn
         
##1.pop()-->syntax--->vn.pop()
         
#we remove random element
         
x
         
{1, 'a', 'D', 100, 'p', 'h', 'y', 'o', 200, 300, 'n', 't'}
x.pop()
         
1
x.pop()
         
'a'
x.pop()
         
'D'
x.pop()
         
100

#remove()--->
         
#to remove selected element
         
#syntax-->vn.remove(element)
         
x
         
{'p', 'h', 'y', 'o', 200, 300, 'n', 't'}
x.remove(300)
         
x
         
{'p', 'h', 'y', 'o', 200, 'n', 't'}
x.remove('hi')
         
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    x.remove('hi')
KeyError: 'hi'

#discard()
         
#syntax-->vn.discard(element)
         
x
         
{'p', 'h', 'y', 'o', 200, 'n', 't'}
x.remove(0)
         
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    x.remove(0)
KeyError: 0
x.discard(0)
         
#claer()
         
#syntax-->vn.clear()
         
x
         
{'p', 'h', 'y', 'o', 200, 'n', 't'}
x.clear()
         
x
         
set()
#del vn
         
x
         
set()
del x
         
x
         
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    x
NameError: name 'x' is not defined
#it will delete x from its memory loaction.
         


#inersection()
         
#symmetric-difference()
         
#difference()
         
#inersection()-->syntax--->set1.intersection(set2)
         
#no common element set will empty
         
#to find common element
         
x
         
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    x
NameError: name 'x' is not defined
x
         
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    x
NameError: name 'x' is not defined
x={1,2,3,4}
         
y={1,33,4}
         
x.intersection(y)
         
{1, 4}
x={1,2,3,4}
         
y={7,8}
         
x.intersection(y)
         
set()

##symmetric-difference()--->syntax--->set1.symmetric_difference(set2)
         
x={1,2,3,4}y={7,8}
         
SyntaxError: invalid syntax
x={1,2,3,4}
         
y={7,8}
         
x.symmetric_difference(y)
         
{1, 2, 3, 4, 7, 8}
##difference()--->syntax--->set1.difference(set2)
         
x={'apple','pen','hii',2,34}
         
y={'apple','hii',22,3}
         
x.difference(y)
         
{2, 'pen', 34}
y.difference(x)
         
{3, 22}

#boolean
         
#isdigit()
         
#issuperset()
         
#issubset()
         
#isdigit()--->syntax-->vn1.isdigit(vn2)
         
#1isdisjoint()--->syntax-->vn1.isdisjoint(vn2)
         
x={1,2,3}
         
y={4,5}
         
x.disjoint(y)
         
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    x.disjoint(y)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
x.isdisjoint(y)
         
True
x={1,2,3}
         
y={4,5,1}
         
x.disjoint(y)
...          
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    x.disjoint(y)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
>>> x.isdisjoint(y)
...          
False
>>> False
...          
False
>>> x
...          
{1, 2, 3}
>>> x.pop(2)
...          
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    x.pop(2)
TypeError: set.pop() takes no arguments (1 given)
>>> x.remove(2)
...          
>>> x
...          
{1, 3}
>>> x.pop()
...          
1
>>> x
...          
{3}
