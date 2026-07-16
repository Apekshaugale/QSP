Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=[100, 50, 400, 500]
a[1]=200
a
[100, 200, 400, 500]
a.append(600)
a
[100, 200, 400, 500, 600]
a.index(600,2)
4
a.index(300,2)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.index(300,2)
ValueError: list.index(x): x not in list
a.insert(300,2)
a
[100, 200, 400, 500, 600, 2]
a.pop(2)
400
a.append(400)
a
[100, 200, 500, 600, 2, 400]
a.remove(2)
a
[100, 200, 500, 600, 400]
a.insert(300,2)
a
[100, 200, 500, 600, 400, 2]
a.remove(2)
a.append(400)
a
[100, 200, 500, 600, 400, 400]
a.remove(400)
a.insert(2,300)
a
[100, 200, 300, 500, 600, 400]
#Exercise 3. Sum and Average of All Numbers in a List
a=[10, 20, 30, 40, 50]
len(a)
5
sum(a)
150
b=sum(a)/5
b
30.0
#Exercise 4. Find Maximum and Minimum from List
b=[45, 12, 89, 2, 67]
min(b)
2
max(b)
89
#Exercise 5. Calculate the Product of All Elements
c
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    c
NameError: name 'c' is not defined
c=[2, 3, 5, 7]
c=2*3*5*7
c
210
#exercise 6. Count Even and Odd Numbers
a=[10, 21, 4, 45, 66, 93, 11]
xercise 7. Reverse a List
SyntaxError: invalid syntax
a=[100, 200, 300, 400, 500]
a.reverse
<built-in method reverse of list object at 0x0000029CE8D9CBC0>
a.reverse()
a
[500, 400, 300, 200, 100]

#Exercise 8. Sort a List of Numbers
Unsorted=[56, 12, 89, 3, 22]
Unsorted.sort()
Unsorted
[3, 12, 22, 56, 89]
#Exercise 9. Create a Copy of a List
a=["Apple", "Banana", "Cherry"]
b=a
b
['Apple', 'Banana', 'Cherry']
a
['Apple', 'Banana', 'Cherry']
#Exercise 10. Combine Two Lists
KeyboardInterrupt
A=["Physics", "Chemistry"]
B=["Maths", "Biology"]
A+B
['Physics', 'Chemistry', 'Maths', 'Biology']
A.append(B)
A
['Physics', 'Chemistry', ['Maths', 'Biology']]
A.extend(B)
A
['Physics', 'Chemistry', ['Maths', 'Biology'], 'Maths', 'Biology']
B
['Maths', 'Biology']
A.pop(['Maths', 'Biology'])
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    A.pop(['Maths', 'Biology'])
TypeError: 'list' object cannot be interpreted as an integer
>>> A.pop(2)
['Maths', 'Biology']
>>> A
['Physics', 'Chemistry', 'Maths', 'Biology']
>>> #Exercise 11. List Slicing: Extract Middle Elements
>>> a=[10, 20, 30, 40, 50, 60, 70]
>>> a=[2:5:1]
SyntaxError: invalid syntax
>>> [2:5:1]
SyntaxError: invalid syntax
>>> a[2:5:1]
[30, 40, 50]
>>> #Exercise 12. Swap Two Elements at Given Indices
>>> a=[23, 65, 19, 90]
>>> a[2]=23
>>> a
[23, 65, 23, 90]
>>> a[0]=19
>>> a
[19, 65, 23, 90]
>>> #Exercise 13. Access Nested Lists (Simple Indexing)
>>> a=[[1, 2], [3, 4, 5], [6, 7]]
>>> a[1][2]
5
>>> #Exercise 14. Check if List Contains a Specific Item
>>> a=["Laptop", "Mouse", "Monitor", "Keyboard"]
