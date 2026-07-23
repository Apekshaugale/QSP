Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#membership operator
#it will check whether the specified value is present in collection or not.
#output in boolean form.


#There are true types-->
#                     1.in operator
#                     2.not operator



#                     1.in operator:It will give the result as a True only if the value is present in the collection.
#   Syntax---> value in collection.
#     we can check   1.value in collection.
#                  2.collection in nested collection    but not collection in collation and value in individual dat type.



3 in 36847
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    3 in 36847
TypeError: argument of type 'int' is not a container or iterable

20 in (20,489,540)
True

 10 in (8397)
 
SyntaxError: unexpected indent
10 in (87,567,7)
False

[8,4] in [87,5,8,4]
False

[8,4] in [87,5,[8,4]]
True




#not in operator
#             It will give the result as True only if value is not present in collection.
>>> #syntax---->value not in colection
>>> 
>>> 
>>> 4 not in (2,4,5,6)
False
>>> 
>>> (5,6) not in (2,4,(5,6))
False
>>> 
>>> [5,6] not in (2,4,[5,6])
False
>>> 
>>> [5,6] not in [2,4,[6]]
True
>>> 
>>> (5,6) not in (2,4,(5))
True
>>> 
>>> '3'in '549023'
True
>>> 
>>> 3 in 6879
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    3 in 6879
TypeError: argument of type 'int' is not a container or iterable
>>> 
>>> '3'not in '549023'
False
>>> 
