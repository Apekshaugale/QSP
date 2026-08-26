Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=
SyntaxError: invalid syntax
#dictionary
a={100:200,'python':'html',74:4554}
a[1]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a[1]
KeyError: 1
#we can not to indexing and slicing in dictionary

a[500]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a[500]
KeyError: 500
del a
a
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a[500]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a[500]
NameError: name 'a' is not defined
>>> a={100:200,'python':'html',74:4554}
>>> a.get(100)
200
>>> a.get(1000,'false')
'false'
>>> a.setdefault(1000)
>>> a
{100: 200, 'python': 'html', 74: 4554, 1000: None}
>>> a.setdefault(100)
200
>>> a.keys()
dict_keys([100, 'python', 74, 1000])
>>> a.values()
dict_values([200, 'html', 4554, None])
>>> a.items()
dict_items([(100, 200), ('python', 'html'), (74, 4554), (1000, None)])
>>> 
>>> #foe adding
>>> #update
>>> #suntax-->vn.update(key,default value)
>>> #without using inbulid function
>>> #vn[key]=value
>>>  #for update
