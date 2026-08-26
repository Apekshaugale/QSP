Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dictionary---> syntax-->vn={key:value,...}
#combination of key and value pair
#boundary condition{}
#internally represented as dict()
#how to create empty dictnpoary normal way
a={}
a
{}

#how to create empty dic using obj
e=dict()
e
{}

e={10:100,78:900,200:2903,100:200}
e[78}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['

e[78]
900
e[200]
2903

#key and value syntsx
e
{10: 100, 78: 900, 200: 2903, 100: 200}
#1.vn[key]
#2.grt()
#vn.get(key,dafault  value)
e.get(333)
e.get(333,"think")
'think'
#set default
#vn.setdefault(key,defaultvalue)
e
{10: 100, 78: 900, 200: 2903, 100: 200}
e[10]
100
e.get(100)
200
e.setdefault(100)
200
e[1000]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    e[1000]
KeyError: 1000
e.get(1000)
#blank space
e.get(1000,''blank space)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
e.get(1000,'blank space')
'blank space'
e.setdefault(1000)
e
{10: 100, 78: 900, 200: 2903, 100: 200, 1000: None}
#it add to dictionary with none value
e.setdefault(1000,'hiii')#i pass default value
e.setdefault(1000,'hiii')
e
{10: 100, 78: 900, 200: 2903, 100: 200, 1000: None}
e.setdefault(1000,'hiii')
e
{10: 100, 78: 900, 200: 2903, 100: 200, 1000: None}
e.setdefault(3000,'hiii')
'hiii'
e
{10: 100, 78: 900, 200: 2903, 100: 200, 1000: None, 3000: 'hiii'}

#in key part if we use duplicate element it will always takes latest one
e={1:1000,True:200,20:780990,20:78}
e
{1: 200, 20: 78}

w={30:'python',40:'mathematics'}
e[30]
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    e[30]
KeyError: 30


W={10:100,78:900,234:899,100:200}
w
{30: 'python', 40: 'mathematics'}
w={10:100,78:900,234:899,100:200}
w
{10: 100, 78: 900, 234: 899, 100: 200}
w.values()
dict_values([100, 900, 899, 200])
#to print only va;lie
w.keys()
dict_keys([10, 78, 234, 100])
#when we wanr only keys

#when wewant complete dic
w.items()
dict_items([(10, 100), (78, 900), (234, 899), (100, 200)])
#output in form of tuples


#in dectionary data type we have want to add element in it
#syntax-->vn[key]=value
#syntax2-->vn.update({key:value})
a={}
a
{}
#syntax-->vn[key]=value we can add only one one pair ata time
#syntax2-->vn.update({key:value}) unli mited ata atime
a[80]='hello'
a
{80: 'hello'}
a[20]=80
a
{80: 'hello', 20: 80}
a.update({200:300})
a
{80: 'hello', 20: 80, 200: 300}
a.update({200:300,80: 'hello', 20: 80})
a
{80: 'hello', 20: 80, 200: 300}
a.update({200:300,80: 'hello', 50: 80})
a
{80: 'hello', 20: 80, 200: 300, 50: 80}
a.pop()
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop(80)
'hello'
a
{20: 80, 200: 300, 50: 80}
a.pop()
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0


#copy
e={1:2,3:4,5:6}
k=e
e
{1: 2, 3: 4, 5: 6}
k
{1: 2, 3: 4, 5: 6}
id(e)
1815064739776
id(k)
1815064739776

e[k]=50
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    e[k]=50
TypeError: cannot use 'dict' as a dict key (unhashable type: 'dict')
e[10]=50
e
{1: 2, 3: 4, 5: 6, 10: 50}
k
{1: 2, 3: 4, 5: 6, 10: 50}
e['pyhon']='hello'
e
{1: 2, 3: 4, 5: 6, 10: 50, 'pyhon': 'hello'}
k
{1: 2, 3: 4, 5: 6, 10: 50, 'pyhon': 'hello'}
k.update({'a':'b'})
e
{1: 2, 3: 4, 5: 6, 10: 50, 'pyhon': 'hello', 'a': 'b'}
k
{1: 2, 3: 4, 5: 6, 10: 50, 'pyhon': 'hello', 'a': 'b'}
e+k
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    e+k
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

#pipeline operator
e|k
{1: 2, 3: 4, 5: 6, 10: 50, 'pyhon': 'hello', 'a': 'b'}
#pipeline operator(|)
e|k
{1: 2, 3: 4, 5: 6, 10: 50, 'pyhon': 'hello', 'a': 'b'}
>>> 
>>> #go for unpacking
>>> #-->**
>>> x={**a,**b}
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    x={**a,**b}
NameError: name 'b' is not defined
>>> x={**e,**k}
>>> x
{1: 2, 3: 4, 5: 6, 10: 50, 'pyhon': 'hello', 'a': 'b'}
>>> #when use single start it take only values
>>> NameError: name 'b' is not defined
SyntaxError: invalid syntax
NameError: name 'b' is not defined

... 
>>> 

>>> 
... 
>>> 

>>> 

... 
... 
>>> 

>>> 

... 



































































