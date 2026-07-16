Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Exercise 14. Check if List Contains a Specific Item
a=["Laptop", "Mouse", "Monitor", "Keyboard"]
print(a.count('Table'))
0
print( 'Table is present or not':a.count('Table'))
SyntaxError: invalid syntax
print( 'Table is present or not:'a.count('Table'))
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print( "Table is present or not:",a.count('Table'))
Table is present or not: 0
print( 'Table is present or not:',a.count('Table'))
Table is present or not: 0
( 'Table is present or not:',a.count('Table'))
('Table is present or not:', 0)
'Table is present or not:',a.count('Table')
('Table is present or not:', 0)
#Exercise 15. Find the Longest String in a List
a=["PHP", "Exercises", "Backend", "Python"]
max(a)
'Python'
max(len(a))
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    max(len(a))
TypeError: 'int' object is not iterable
max(len('a'))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    max(len('a'))
TypeError: 'int' object is not iterable
a=[1, 2, 3, 4, 5]
a=a*a
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a=a*a
TypeError: can't multiply sequence by non-int of type 'list'
#Exercise 17. Count Occurrences of an Item
a=[10, 20, 30, 10, 40, 10, 50]
a.count('a')
0
a.count('10')
0
a.count(10)
3
print('count of 10 is:',a.count(10))
count of 10 is: 3
#Exercise 18. Remove All Occurrences of a Specific Item
a=[5, 20, 15, 20, 25, 50, 20]
print("Cleaned List:",a.remove(20))
Cleaned List: None
print("Cleaned List:",a.remove('20'))
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print("Cleaned List:",a.remove('20'))
ValueError: list.remove(x): x not in list
a.remove(20)
a
[5, 15, 25, 50, 20]
a.remove(20)
a
[5, 15, 25, 50]
print("Cleaned List:",a)
Cleaned List: [5, 15, 25, 50]
a=[5, 20, 15, 20, 25, 50, 20]
a.remove(20,2)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a.remove(20,2)
TypeError: list.remove() takes exactly one argument (2 given)

#Exercise 19. Remove Empty Strings from a List of Strings
a=["Mike", "", "Emma", "Kelly", "", "Brad"]
a.remove( "")
a
['Mike', 'Emma', 'Kelly', '', 'Brad']
a.remove( "")
a
['Mike', 'Emma', 'Kelly', 'Brad']
List=[10, 20, 10, 30, 40, 40, 20, 50]
dict.fromkeys(list)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    dict.fromkeys(list)
TypeError: 'type' object is not iterable
dict.fromkeys('List')
{'L': None, 'i': None, 's': None, 't': None}
 List=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
SyntaxError: unexpected indent
List=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(List%2==0)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print(List%2==0)
TypeError: unsupported operand type(s) for %: 'list' and 'int'
print(List/2==0)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print(List/2==0)
TypeError: unsupported operand type(s) for /: 'list' and 'int'
#Exercise 22. Concatenate Two Lists Index-wise
#Exercise 22. Concatenate Two Lists Index-wise
#Exercise 24. Add New Item After a Specified Item
List=[10, 20, 30, 40, 50]
List.insert(3,35)
List
[10, 20, 30, 35, 40, 50]
print('Updated List: ',List.insert(3,35))
Updated List:  None
print('Updated List: ',List)
Updated List:  [10, 20, 30, 35, 35, 40, 50]
list.remove(35)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    list.remove(35)
TypeError: descriptor 'remove' for 'list' objects doesn't apply to a 'int' object
list.remove('35')
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    list.remove('35')
TypeError: descriptor 'remove' for 'list' objects doesn't apply to a 'str' object
>>> List.remove(35)
>>> print('Updated List: ',List)
Updated List:  [10, 20, 30, 35, 40, 50]
>>> #Exercise 25. Replace List’s Item with New Value if Found
>>> a=[5, 10, 15, 20, 25]
>>> print('find :',a[3])
find : 20
>>> print('Replace with:',a[3]=200)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> a[3]=200
>>> print('Replace with:',a)
Replace with: [5, 10, 15, 200, 25]
>>> a=[1, 3, 3, 2, 1, 1, 4, 3, 3]
>>> max(a)
4
>>> max(count(a))
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    max(count(a))
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> max(round(a))
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    max(round(a))
TypeError: type list doesn't define __round__ method
