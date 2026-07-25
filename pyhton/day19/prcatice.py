Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d = {"x": 10, "y": 20}
print(list(d.items()))
[('x', 10), ('y', 20)]
print(d.items())
dict_items([('x', 10), ('y', 20)])
d.items()
dict_items([('x', 10), ('y', 20)])
x = "hello"
print("HELLO".lower() == x)
True
print(x[5])
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(x[5])
IndexError: string index out of range
l = [[1, 2], [3, 4], [5, 6]]
print(3 in l)
False
print(3 in l[1])
True
l = [1, 2, 2, 3, 2, 4, 2]
print(l.count(2))
4
l = [1, 2, 3, 4]
>>> result = l.reverse()
>>> print(result)
None
>>> l = [1, 2, 3]
>>> l.clear()
>>> print(l)
[]
>>> t1 = (1, 2, 3)
>>> t2 = (4, 5)
>>> print(t1 + t2)
(1, 2, 3, 4, 5)
>>> 
>>> t = (1, 2)
>>> print(t * "3")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(t * "3")
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
>>> KeyboardInterrupt
>>> d = {"a": 1, "b": 2}
>>> print("a" in d)
True
>>> print(1 in d)
False
>>> d = {"a": 10, "b": 20, "c": 30}
>>> print(sum(d.values()))
60
