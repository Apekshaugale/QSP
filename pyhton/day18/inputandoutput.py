Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Input and output
#1.Input --->it is inbulid method used to take input from users.


#syntax-->var=datatype(input('msg'))

#ex-->a=int(input('enter name'))

#by default input() will take string as default value.

#eval()-->it ia inbuild function used to take input from the user,specially for collection data type.

#syntax--->var=eval(input('msg'))

c=eval(input('enter int data:'))
enter int data:jgohp
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    c=eval(input('enter int data:'))
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'jgohp' is not defined
print(c,type(c))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(c,type(c))
NameError: name 'c' is not defined

c=eval(input('enter int data:'))
enter int data:'string'
print(c,type(c))
string <class 'str'>
>>> 
>>> c=eval(input('enter int data:'))
enter int data:[12,45,66]
>>> print(c,type(c))
[12, 45, 66] <class 'list'>
>>> 
>>> c=eval(input('enter int data:'))
enter int data:(1,2,4,5)
>>> print(c,type(c))
(1, 2, 4, 5) <class 'tuple'>
>>> 
>>> c=bool(input('Enter bool value:'))
Enter bool value:3
>>> print(c,type(c))
True <class 'bool'>
>>> 
>>> c=int(input('Enter integer value:'))
Enter integer value:34
>>> print(c,type(c))
34 <class 'int'>
>>> 
>>> c=float(input('Enter float value:'))
Enter float value:3.5
>>> print(c,type(c))
3.5 <class 'float'>
>>> 
>>> c=complex(input('Enter complex value:'))
Enter complex value:2+3j
>>> print(c,type(c))
(2+3j) <class 'complex'>
