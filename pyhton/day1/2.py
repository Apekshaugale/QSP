Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Identifier
#rule-->
#identifier is nothing but the name of the python progrem like variable,module,object,fubction.
#rule-->1
#In identifier part we can use alphabet means upper,lower or combinatin of both
xyz=123
xyz
123

xYz=12
xYz
12

#rule2-->
#In identifier part should not start with number but we can use numbers in between or last.

34h="hi"
SyntaxError: invalid decimal literal

av='hi'
av
'hi'

#rule3--.>
#In identifier part we can not used special character except underscore.
first_class=23
first_class
23

_50=aa
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    _50=aa
NameError: name 'aa' is not defined. Did you mean: 'av'?
-50=123
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
_50=123
_50
123

#rule4-->
>>> #In identifier part we can't used keywords .
>>> 
>>> in=34
SyntaxError: invalid syntax
>>> 
>>> In=34
>>> In
34
>>> 
>>> #Rule5-->
>>> #In identifier parts we can pass unlimited characters but according to PEP8 rule we can pass 79 characters.
>>> 
>>> #how to check whether the given identifier rule is true or false?
>>> #--->"identifier_part".isidentifier()
>>> 
>>> #Note-->if the rule is vaild it gives : True
>>> #       if the rule is invaild it gives : False
>>> 
>>> "cash".isidentifier()
True
>>> 
>>> '-'.isidentifier()
False
>>> 
>>> '_'.isindentifer()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    '_'.isindentifer()
AttributeError: 'str' object has no attribute 'isindentifer'. Did you mean: 'isidentifier'?
>>> 
>>> 
