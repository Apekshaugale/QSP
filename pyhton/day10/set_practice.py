Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

= RESTART: C:/Users/Apeksha/AppData/Local/Programs/Python/Python314/py.py
a='hello pratiksha'
a[0:4+1:1]
'hello'
a[:4+1:]
'hello'
a[9:15+1:1]
'tiksha'
a[9::]
'tiksha'
a[-1::-1]
'ahskitarp olleh'
a[::-1]
'ahskitarp olleh'
a[::1]
'hello pratiksha'
s='hello'
s[::2]
'hlo'
s[1::2]
'el'
# Basic Set Operations
fruits = {"apple", "banana", "cherry"}
print('Add new element:',fruits('mango'))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print('Add new element:',fruits('mango'))
TypeError: 'set' object is not callable
print('Add new element:',fruits.add('mango'))
Add new element: None
fruits.add('mango')
print('Add new element:',fruits)
Add new element: {'apple', 'cherry', 'mango', 'banana'}
fruits.remove('mango')
print('removed:',fruits)
removed: {'apple', 'cherry', 'banana'}
fruits.discard('mango')
print('removed:',fruits)
removed: {'apple', 'cherry', 'banana'}
fruits.discard('apple')
print('removed:',fruits)
removed: {'cherry', 'banana'}

#Exercise 2: Clear All Elements
colors = {"red", "green", "blue"}
colors.clear()
colors
set()

#Exercise 3: Find the Length of a Set
animals = {"cat", "dog", "bird", "fish"}
print('Length of set:',len[animals])
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print('Length of set:',len[animals])
TypeError: 'builtin_function_or_method' object is not subscriptable
len[animals]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    len[animals]
TypeError: 'builtin_function_or_method' object is not subscriptable
animals = {"cat", "dog", "bird", "fish"}
len[animals]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    len[animals]
TypeError: 'builtin_function_or_method' object is not subscriptable
animals={"cat", "dog", "bird", "fish"}
len[animals]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    len[animals]
TypeError: 'builtin_function_or_method' object is not subscriptable
a={"cat", "dog", "bird", "fish"}
len[a]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    len[a]
TypeError: 'builtin_function_or_method' object is not subscriptable
animals = {"cat", "dog", "bird", "fish"}
len(animals)
4
print('Length of set:',len(animals))
Length of set: 4

#Exercise 4: Check if a Set is Empty
data ={}
print('set is empty',data)
set is empty {}

#Exercise 5: Union of Sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_a.union(set_b)
{1, 2, 3, 4, 5, 6}
print('Union',set_a.union(set_b))
Union {1, 2, 3, 4, 5, 6}

#Exercise 6: Intersection of Sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print('INtersection :',set_a.intersection(set_b))
INtersection : {3, 4}

#Exercise 7: Difference of Sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print('INtersection :',set_a.difference(set_b))
INtersection : {1, 2}
print('Difference :',set_a.difference(set_b))
Difference : {1, 2}

#Exercise 8: Symmetric Difference
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print('Symmetric Difference:',set_a.symmetric_difference(set_b))
Symmetric Difference: {1, 2, 5, 6}

#Exercise 9: Find Max and Min
numbers = {42, 7, 19, 85, 3, 56}
print('max:',max(numbers))
max: 85
print('min:',min(numbers))
min: 3

#Exercise 10: Sum of Set Elements
numbers = {10, 20, 30, 40, 50}
print('Sum:',sum(numbers))
Sum: 150

#Exercise 11: Add a List of Elements
fruits = {"apple", "banana"}
new_fruits = ["cherry", "mango", "apple"]
print('Updated set:',fruits.update(new_fruits))
Updated set: None
fruits.update(new_fruits)
fruits
{'apple', 'cherry', 'mango', 'banana'}
print('Updated set:',fruits)
Updated set: {'apple', 'cherry', 'mango', 'banana'}

#Exercise 12: Update with Multiple Iterables
base = {1, 2}
from_list = [3, 4]
from_tuple = (5, 6)
from_set = {7, 8}
base.update(from_list, from_tuple, from_set)
print('Updated set:',base)
Updated set: {1, 2, 3, 4, 5, 6, 7, 8}

#Exercise 13: Check Subset and Superset
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
print('Subset:',set_a.subset(set_b))
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    print('Subset:',set_a.subset(set_b))
AttributeError: 'set' object has no attribute 'subset'. Did you mean: 'issubset'?
print('Subset:',set_a.issubset(set_b))
Subset: True
print('Subset:',set_b.issubset(set_a))
Subset: False
print('Superset of set_a:',set_a.issuperset(set_b))
Superset of set_a: False
print('Superset of set_b:',set_b.issuperset(set_a))
Superset of set_b: True

#Exercise 14: Intersection Check with isdisjoint()
set_a = {1, 2, 3}
set_b = {4, 5, 6}
print('Are the sets disjoint?',set_a.isdisjoint(set_b))
Are the sets disjoint? True
print('Are the sets disjoint?',set_b.isdisjoint(set_a))
Are the sets disjoint? True

#Exercise 15: Set Difference Update
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
print('a:',a.difference(b))
a: {1, 2}

#Exercise 16: Set Intersection Update
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
a.intersection_update(b)
print('set a:',a)
set a: {3, 4, 5}
print('set b:',b)
set b: {3, 4, 5, 6, 7}
b.intersection_update(a)
print('set a:',a)
set a: {3, 4, 5}
print('set b:',b)
set b: {3, 4, 5}
b.intersection_update(a)
print('set a:',a)
set a: {3, 4, 5}

#Exercise 17: Set Symmetric Difference Update
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
a.symmetric_difference_update(b)
print('set a:',a)
set a: {1, 2, 6, 7}

print('set b:',b)
set b: {3, 4, 5, 6, 7}
b.symmetric_difference_update(a)
print('set b:',b)
set b: {1, 2, 3, 4, 5}
print('set a:',a)
set a: {1, 2, 6, 7}
b.symmetric_difference_update(a)
print('set b:',b)
set b: {3, 4, 5, 7, 6}
a.symmetric_difference_update(b)
print('set a:',a)
set a: {1, 2, 4, 3, 5}

#Exercise 18: Remove Items Simultaneously
items = {10, 20, 30, 40, 50, 60}
remove.items(20,40,60)
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    remove.items(20,40,60)
NameError: name 'remove' is not defined
items.remove(20,40,60)
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    items.remove(20,40,60)
TypeError: set.remove() takes exactly one argument (3 given)
items = {10, 20, 30, 40, 50, 60}
to_remove = {20, 40, 60}
items.difference(to_remove)
{50, 10, 30}
items.difference_update(to_remove)
items
{50, 10, 30}

#Exercise 19: The Pop Operation
s = {100, 200, 300}
remove(100)
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    remove(100)
NameError: name 'remove' is not defined. Did you mean: 'to_remove'?
s.remove(100)
s
{300, 200}
s.clear()
s
set()

#Exercise 20: Filter a Set
n= {1, 2, 3, 6, 7, 9, 12, 14, 15}
n[2::2]
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    n[2::2]
TypeError: 'set' object is not subscriptable

#Exercise 21: Find Common Elements in Lists
list1 = [1, 2, 3, 4, 5, 3, 2]
list2 = [3, 4, 5, 6, 7, 4, 5]
print('common:',list1.intersection(list2))
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    print('common:',list1.intersection(list2))
AttributeError: 'list' object has no attribute 'intersection'
list1.intersection(list2)
Traceback (most recent call last):
  File "<pyshell#167>", line 1, in <module>
    list1.intersection(list2)
AttributeError: 'list' object has no attribute 'intersection'
set(list1)
{1, 2, 3, 4, 5}
set(list2)
{3, 4, 5, 6, 7}
print('common:',list1.intersection(list2))
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    print('common:',list1.intersection(list2))
AttributeError: 'list' object has no attribute 'intersection'
list1
[1, 2, 3, 4, 5, 3, 2]
aset(list1)
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    aset(list1)
NameError: name 'aset' is not defined. Did you mean: 'set'?
a=set(list1)
b=set(list2)
a
{1, 2, 3, 4, 5}
b
{3, 4, 5, 6, 7}
print('common:',list1.intersection(list2))
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    print('common:',list1.intersection(list2))
AttributeError: 'list' object has no attribute 'intersection'
print('common:',a.intersection(b))
common: {3, 4, 5}
>>> 
>>> #Exercise 20: Filter a Set
>>> #Exercise 21: Find Common Elements in Lists
>>> list1 = [1, 2, 3, 4, 5, 3, 2]
>>> list2 = [3, 4, 5, 6, 7, 4, 5]a=set(list1)
SyntaxError: invalid syntax
>>> list2 = [3, 4, 5, 6, 7, 4, 5]
>>> a=set(list1)
>>> b=set(list2)
>>> a
{1, 2, 3, 4, 5}
>>> bprint('common:',a.intersection(b))
Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    bprint('common:',a.intersection(b))
NameError: name 'bprint' is not defined. Did you mean: 'print'?
>>> print('common:',a.intersection(b))
common: {3, 4, 5}
>>> 
>>> #Exercise 22: Count Unique Words
>>> text = "the cat sat on the mat the cat"
>>> text.count('t')
7
>>> v=set(text)
>>> v
{' ', 'o', 'a', 't', 's', 'h', 'n', 'c', 'e', 'm'}
>>> 
>>> #Exercise 23: Convert Set to Joined String
