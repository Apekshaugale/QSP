Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="PYTHON IS AWESOME"
a.lower()
'python is awesome'
a="data science"
a.lower()
'data science'
a.title()
'Data Science'
a.swapcase()
'DATA SCIENCE'
a
'data science'
a'"welcome to machine learning"
SyntaxError: unterminated string literal (detected at line 1)
a="welcome to machine learning"
a.swapcase()
'WELCOME TO MACHINE LEARNING'
a.capitalize()
'Welcome to machine learning'
a.count('a')
2
a.count('a',13)
1
a.islower()
True

a.isupper()
False
a.istitle()
False
a.isalpha()
False
a
'welcome to machine learning'
a.isalpha()
False
a="Python123"
a.isalnum()
True
a.isnum()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.isnum()
AttributeError: 'str' object has no attribute 'isnum'. Did you mean: 'isalnum'?
a.isdigit()
False
a="student@gmail.com"
a.endswiths('.com')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.endswiths('.com')
AttributeError: 'str' object has no attribute 'endswiths'. Did you mean: 'endswith'?
a.endswith('.com')
True
a.startswith('.com',13,17)
True
a.endswith('stu',0,3)
True
a="Python Programming"
a.index("gram")
10
a.rindex('a')
12
a="banana"
a.rindex('a')
5
a.rindex('a',2)
5
a="python java c++"
a.find('java')
7
a.rfind('a',2)
10
a="hello world"
a.rfind('a')
-1
a.rfind('0o')
-1
a.rfind('o')
7
a.find('o')
4
a="cat likes milk"
a.replace('cat','dog')
'dog likes milk'
a=['P','Y','T','H','O','N']
'-'.joint(,)
SyntaxError: invalid syntax
'-'.joint(',')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    '-'.joint(',')
AttributeError: 'str' object has no attribute 'joint'. Did you mean: 'join'?
'-'.join(',')
','
'-'.join('a')
'a'
'-'.join(a)
'P-Y-T-H-O-N'
a="    Python    "
a.strip()
'Python'
a.isspace()
False
a="Python     "
a.rstrip()
'Python'
a="Apple Mango Banana"
a.split()
['Apple', 'Mango', 'Banana']
a="a,b,c,d,e"
a.split()
['a,b,c,d,e']
a.split(',')
['a', 'b', 'c', 'd', 'e']
a="Apple Mango Banana"
a.split(',')
['Apple Mango Banana']
a.split('go')
['Apple Man', ' Banana']
student_name.isidentifier()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    student_name.isidentifier()
NameError: name 'student_name' is not defined
a=student_name
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a=student_name
NameError: name 'student_name' is not defined
a='student_name'
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
a="banana apple mango"
a.upper()
'BANANA APPLE MANGO'
a=a.upper()
a
'BANANA APPLE MANGO'
a.count('A')
5
a="     python programming"
a.lstrip()
'python programming'
a=a.lstrip()
a
'python programming'
a.capitalize()
'Python programming'
a.title()
'Python Programming'
a=a.title()
a.istitle()
True
a="Python is easy"
a.replace(' '.'_')
SyntaxError: invalid syntax
a.replace(' ','_')
'Python_is_easy'
>>> a="HTML,CSS,JS,Python"
>>> " | ".join(a)
'H | T | M | L | , | C | S | S | , | J | S | , | P | y | t | h | o | n'
>>> a="bananas are amazing"
>>> a.find('a')
1
>>> a.rfind('a')
14
>>> a="DataScience123"
>>> a.isalph()
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    a.isalph()
AttributeError: 'str' object has no attribute 'isalph'. Did you mean: 'isalpha'?
>>> a.isalpha()
False
>>> a.isalnum()
True
>>> a="welcome_to_python"
>>> a.replace('_',' ')
'welcome to python'
>>> a=a.replace('_',' ')
>>> a.title()
'Welcome To Python'
>>> a
'welcome to python'
>>> a.replace("_", " ").title()
'Welcome To Python'
