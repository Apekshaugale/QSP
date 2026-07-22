Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a={356,57}
a.add(('python','mjh'))
a
{('python', 'mjh'), 57, 356}
a.add(('5','9'))
a
{('python', 'mjh'), 57, 356, ('5', '9')}
a.add('5','9')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a.add('5','9')
TypeError: set.add() takes exactly one argument (2 given)
a.add((5,9))
a
{('python', 'mjh'), 356, ('5', '9'), (5, 9), 57}
a.update(('5','9'))
a
{('python', 'mjh'), 356, '9', ('5', '9'), (5, 9), 57, '5'}
a.update((['ji','ji']))
a
{('python', 'mjh'), 356, '9', ('5', '9'), (5, 9), 'ji', 57, '5'}
a.update(('python','mjh'))
a
{('python', 'mjh'), 356, '9', 'mjh', ('5', '9'), (5, 9), 'ji', 57, '5', 'python'}
a.update('python','mjh')
a
{'t', 'm', 'o', ('python', 'mjh'), 356, '9', 'mjh', 'n', ('5', '9'), 'h', 'j', 'p', (5, 9), 'ji', 57, '5', 'python', 'y'}
a.update((5,9))
a
{('python', 'mjh'), '9', 5, 9, 'j', 'm', (5, 9), 57, 'y', 'python', 'o', ('5', '9'), 'h', 'p', 'ji', '5', 356, 'mjh', 'n', 't'}
a.update((5,[9]))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.update((5,[9]))
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
a.update([5,9]])
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
a.update([5,9])
a
{('python', 'mjh'), '9', 5, 9, 'j', 'm', (5, 9), 57, 'y', 'python', 'o', ('5', '9'), 'h', 'p', 'ji', '5', 356, 'mjh', 'n', 't'}
a.update([[[5,9]]])
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.update([[[5,9]]])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
a.update(([[5,9]]))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.update(([[5,9]]))
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
a.update(([5,9]))
a
{('python', 'mjh'), '9', 5, 9, 'j', 'm', (5, 9), 57, 'y', 'python', 'o', ('5', '9'), 'h', 'p', 'ji', '5', 356, 'mjh', 'n', 't'}
a.update(((['hellooo'])))
a
{('python', 'mjh'), '9', 5, 9, 'hellooo', 'j', 'm', (5, 9), 57, 'y', 'python', 'o', ('5', '9'), 'h', 'p', 'ji', '5', 356, 'mjh', 'n', 't'}
a.update([[['hellooo']]])
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.update([[['hellooo']]])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')




#intersection
#syntax-->set1.intersection(set2)
#we find common element in both set
a={4,5,7,9}
b={49,8,2,3,5}
a.intersection(b)
{5}
c={68,49,6,4}
a.intersection(b,c)
set()
c={5}
a.intersection(b,c)
{5}
d={2,3,5,4}
a.intersection(b,c,d)
{5}

#intersection update
#syntax-->set1.intersection_update(set2)
a.intersection_update(b,c,d)
a
{5}
b
{49, 2, 3, 5, 8}
c
{5}
d
{2, 3, 4, 5}
a.intersection_update(b,c,d)
a
{5}

#symmetric_difference
#syntax-->set1.symmetric_difference(set2)
#used to find uncommon elent in both set
a={4,5,7,9}
c={68,49,6,4}

b={49,8,2,3,5}
a.symmetric_difference(b)
{49, 2, 3, 4, 7, 8, 9}
a.symmetric_difference(b,c)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a.symmetric_difference(b,c)
TypeError: set.symmetric_difference() takes exactly one argument (2 given)
a.symmetric_difference((b,c))
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a.symmetric_difference((b,c))
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
>>> a.difference(b,c)
{9, 7}
>>> a.difference(b)
{9, 4, 7}
>>> a.isdisjoint(b,c)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a.isdisjoint(b,c)
TypeError: set.isdisjoint() takes exactly one argument (2 given)
>>> a.isdisjoint(b)
False
>>> a.issuperset(b,c)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a.issuperset(b,c)
TypeError: set.issuperset() takes exactly one argument (2 given)
>>> a.issubset(b,c)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    a.issubset(b,c)
TypeError: set.issubset() takes exactly one argument (2 given)
>>> a.issuperset(c)
False
>>> a.issubset(c)
False
>>> a.union(b,c)
{2, 3, 4, 5, 6, 7, 8, 9, 68, 49}
>>> a.union(b,c,d)
{2, 3, 4, 5, 6, 7, 8, 9, 68, 49}
