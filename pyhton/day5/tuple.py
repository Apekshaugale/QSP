Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuples
#it is ordered data type
#it accept duplicate value
#elements are seperated by comma
#boundary condition is not manditory
#comma is manditory
a=a'b'c'd
SyntaxError: unterminated string literal (detected at line 1)
a=abs,b,cc,d
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a=abs,b,cc,d
NameError: name 'b' is not defined
a=a,b,c,d
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a=a,b,c,d
NameError: name 'a' is not defined

#len()--->len(vn)or len(tuple)
#how to create empty tuple in normal way
a=()
a
()

#how to create empty tuple using object
tuple()
()
type(a)
<class 'tuple'>


#how to crreate sinle vue datatype
#single value tuple
a=(300)
type(a)
<class 'int'>
a=900
type(a)
<class 'int'>
a=(900,)
a
(900,)
type(a)
<class 'tuple'>

a=900,
type(a)
<class 'tuple'>
a=b,c,s
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a=b,c,s
NameError: name 'b' is not defined
a='a','d'
#tuple data type aslo immutable data type i.e we can't change original data but we can do modifivation .but











#immutable i want to change
s=(10,20,'HELLO',[1,2,3])
s[0]
10
s[0]=100
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    s[0]=100
TypeError: 'tuple' object does not support item assignment
s[2].lower
<built-in method lower of str object at 0x000002A9BFA2A9A0>
s[2].lower()
'hello'
#list is mutable
s[3]
[1, 2, 3]
s[3][0]=100
s
(10, 20, 'HELLO', [100, 2, 3])


#immutable here we cn't change original odject we we can do midification.
#ex:string,tuplr
#mutable here we can change original data
#Ex:list set dictionary.

t=(34,['abc','walmat','python'],600,{67,909})
t[1]
['abc', 'walmat', 'python']
t[1][1]
'walmat'
t[1][1]=100
t
(34, ['abc', 100, 'python'], 600, {67, 909})
t[1]
['abc', 100, 'python']

e=(100,67,'abc','python','walmart','insat')
e[-3]
'python'

e[100]
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    e[100]
IndexError: tuple index out of range
e[5]
'insat'



w=(100,500,True,False,'snapchat','walmart','market','penset')
#indexing-->varname[position]
#indexing starts from zero
#indexing starts from zero
w[4]
'snapchat'
w[-4]
'snapchat'
w[1]
500
w[-7]
500

w[6]
'market'
w[-2]
'market'

w[0]
100
w[-8]
100

w[20]
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    w[20]
IndexError: tuple index out of range
w[-30]
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    w[-30]
IndexError: tuple index out of range

#slicing
#forward-->vn[si:ei+1:sv]
w
(100, 500, True, False, 'snapchat', 'walmart', 'market', 'penset')
w[1:5:1]
(500, True, False, 'snapchat')
')
w[-7:-4:-1]
SyntaxError: unterminated string literal (detected at line 1)
w[-7:-4:-1]
()
w[0:7:2]
(100, True, 'snapchat', 'market')
#indexing+silicing
w[4]
'snapchat'
w[4][4:8:1]
'chat'
w[6][1:4:1]
'ark'
w[5][0:7:7]
'w'
w[5][0:7:6]
'wt'
w[4][2:7:2]
'aca'
w[7][0:6:5]
'pt'

r=('India','Abroad','classes','germany','Australia','canada')
#road
r[1]
'Abroad'
r[1][2:6:1]
'road'
#ses
r[2][4:8:1]
'ses'
#any
r[3][4:7:1]
'any'
#lia
r[5][6:9:1]
''
r[4][6:9:1]
'lia'
#ada
r[5][3:6:1]
'ada'
#('Abroad','classes')
r[1:3:1]
('Abroad', 'classes')
>>> r[0:5:2]
('India', 'classes', 'Australia')
>>> 
>>> 
>>> #count
>>> #syntax-->vn.count('caharcter')
>>> e
(100, 67, 'abc', 'python', 'walmart', 'insat')
>>> r
('India', 'Abroad', 'classes', 'germany', 'Australia', 'canada')
>>> #noly one arugument can pass no two argument
>>> r.coun('Inadia')
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    r.coun('Inadia')
AttributeError: 'tuple' object has no attribute 'coun'. Did you mean: 'count'?
>>> r.count('India')
1
>>> 
>>> t=(10,20,10,30,10)
>>> y.count('10')
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    y.count('10')
NameError: name 'y' is not defined
>>> t.count('10')
0
>>> t.count(10)
3
>>> #string count method -->
