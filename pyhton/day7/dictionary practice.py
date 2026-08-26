Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
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

SyntaxError: invalid syntax
#for update
#syntax-->vn.update({key:value})
a
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a
NameError: name 'a' is not defined
a={100:200,'python':'html',74:4554}
a.update({45:68})
a
{100: 200, 'python': 'html', 74: 4554, 45: 68}
a.pop()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop(600)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a.pop(600)
KeyError: 600
a.pop(600,'true')
'true'
a.pop(100)
200
a
{'python': 'html', 74: 4554, 45: 68}
a.popitems()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.popitems()
AttributeError: 'dict' object has no attribute 'popitems'. Did you mean: 'popitem'?
a.popitem()
(45, 68)
a
{'python': 'html', 74: 4554}
a.clear()
a
{}
dir a
SyntaxError: invalid syntax
del a
a
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a
NameError: name 'a' is not defined
a={100: 200, 'python': 'html', 74: 4554, 45: 68}
a[100]
200
a[1000]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a[1000]
KeyError: 1000
a
{100: 200, 'python': 'html', 74: 4554, 45: 68}
a.get(100)
200
a.get(1000)
a
{100: 200, 'python': 'html', 74: 4554, 45: 68}
a.setdefault(1000)
a
{100: 200, 'python': 'html', 74: 4554, 45: 68, 1000: None}
a.values()
dict_values([200, 'html', 4554, 68, None])
a.update({90:88})
a
{100: 200, 'python': 'html', 74: 4554, 45: 68, 1000: None, 90: 88}
a.update({(90:88),(90:8),(90:80)})
SyntaxError: invalid syntax
a.update({90:88,90:8,90:80)})
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
a.update({90:88,90:8,90:80})
a
{100: 200, 'python': 'html', 74: 4554, 45: 68, 1000: None, 90: 80}
a.update({90:88,91:8,9:80})
a
{100: 200, 'python': 'html', 74: 4554, 45: 68, 1000: None, 90: 88, 91: 8, 9: 80}
a.pop
<built-in method pop of dict object at 0x0000021B1368FD80>
a.pop()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop(100)
200
a
{'python': 'html', 74: 4554, 45: 68, 1000: None, 90: 88, 91: 8, 9: 80}
a.pop(600)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a.pop(600)
KeyError: 600
a
{'python': 'html', 74: 4554, 45: 68, 1000: None, 90: 88, 91: 8, 9: 80}
a.pop(600,has)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a.pop(600,has)
NameError: name 'has' is not defined. Did you mean: 'hash'?
a.pop(600,'has')
'has'
a.update({90:88,91:8,9:80})
a
{'python': 'html', 74: 4554, 45: 68, 1000: None, 90: 88, 91: 8, 9: 80}
a.popitem()
(9, 80)
b=a
b
{'python': 'html', 74: 4554, 45: 68, 1000: None, 90: 88, 91: 8}
a
{'python': 'html', 74: 4554, 45: 68, 1000: None, 90: 88, 91: 8}
id(a)
2315313020288
id(b)
2315313020288
dict.fromkeys(a)
{'python': None, 74: None, 45: None, 1000: None, 90: None, 91: None}
a.fromkeys(b)
{'python': None, 74: None, 45: None, 1000: None, 90: None, 91: None}
a.fromkeys(a)
{'python': None, 74: None, 45: None, 1000: None, 90: None, 91: None}
dict.fromkeys(a,'me')
{'python': 'me', 74: 'me', 45: 'me', 1000: 'me', 90: 'me', 91: 'me'}
a
{'python': 'html', 74: 4554, 45: 68, 1000: None, 90: 88, 91: 8}
a.fromkeys(b,'me')
{'python': 'me', 74: 'me', 45: 'me', 1000: 'me', 90: 'me', 91: 'me'}
a
{'python': 'html', 74: 4554, 45: 68, 1000: None, 90: 88, 91: 8}
b
{'python': 'html', 74: 4554, 45: 68, 1000: None, 90: 88, 91: 8}
a.find(1)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a.find(1)
AttributeError: 'dict' object has no attribute 'find'
a=[44,5,23,45]
a.find(2)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a.find(2)
AttributeError: 'list' object has no attribute 'find'
a='44,5,23,45'
a.find(2)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    a.find(2)
TypeError: find() argument 1 must be str, not int
a='python'
a.find(2)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a.find(2)
TypeError: find() argument 1 must be str, not int
a.find('2')
-1
a='44,5,23,45'
a.find('2')
5
a="a,b,c,d,e"
a.split(',')
['a', 'b', 'c', 'd', 'e']
a.split('')
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a.split('')
ValueError: empty separator
a.split(' ')
['a,b,c,d,e']
a.split(' -')
['a,b,c,d,e']
a="student_name"
a.isidentifier()
True
import keyword
keyword.iskeyword("while")
True
a="      "
a.isspace()
True
a="https://google.com"
a.removeprefix("https://")
'google.com'
a="flower.jpg"
a.removesuffix(".jpg")
'flower'
a="Python is easy"
'_'.joint(' ')
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    '_'.joint(' ')
AttributeError: 'str' object has no attribute 'joint'. Did you mean: 'join'?
'_'.join(' ')
' '
'_'.join(a)
'P_y_t_h_o_n_ _i_s_ _e_a_s_y'
a
'Python is easy'
a.replace(' ',' -')
'Python -is -easy'
a.replace(' ','-')
'Python-is-easy'
a="HTML,CSS,JS,Python"
a.spilt('|')
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    a.spilt('|')
AttributeError: 'str' object has no attribute 'spilt'. Did you mean: 'split'?
a.split('|')
['HTML,CSS,JS,Python']
a.split('|',',')
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    a.split('|',',')
TypeError: 'str' object cannot be interpreted as an integer
a.split()
['HTML,CSS,JS,Python']
a=a.split()
a
['HTML,CSS,JS,Python']
'|'.join(a)
'HTML,CSS,JS,Python'
'|'.join(a.split())
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    '|'.join(a.split())
AttributeError: 'list' object has no attribute 'split'
a.replace(',','-')
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    a.replace(',','-')
AttributeError: 'list' object has no attribute 'replace'
a.split(',')
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    a.split(',')
AttributeError: 'list' object has no attribute 'split'
a= "HTML,CSS,JS,Python"
a.split(',')
['HTML', 'CSS', 'JS', 'Python']
" | ".join(a.split(','))
'HTML | CSS | JS | Python'
a="bananas are amazing"
a.find('a')
1
a.rfind('a')
14
a="resume.pdf"
a.removesuffix('.pdf')
'resume'
a=a.removesuffix('.pdf')
a
'resume'
>>> a.startswith('resume')
True
>>> a="DataScience123"
>>> a.isaplha()
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    a.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
>>> a.isalpha()
False
>>> a.isalnum()
True
>>> a=
SyntaxError: invalid syntax
>>> a="python programming"
>>> a.title()
'Python Programming'
>>> a=a.title()
>>> a.swapcase()
'pYTHON pROGRAMMING'
>>> a="   Learn AI   "
>>> a.split()
['Learn', 'AI']
>>> a.strip()
'Learn AI'
>>> a=a.strip()
>>> a.endswith('AI')
True
>>> a="education"
