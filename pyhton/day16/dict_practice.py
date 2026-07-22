Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a={7:9,89:09}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
a={7:9,89:9}
a
{7: 9, 89: 9}
a[8]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a[8]
KeyError: 8
a.get(7)
9
>>> a.update('puyhon')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a.update('puyhon')
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> a.update({'puyhon'})
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.update({'puyhon'})
ValueError: dictionary update sequence element #0 has length 6; 2 is required
>>> a.update({'puyhon':9})
>>> a
{7: 9, 89: 9, 'puyhon': 9}
>>> a[3]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a[3]
KeyError: 3
>>> a[2]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a[2]
KeyError: 2
>>> keys()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    keys()
NameError: name 'keys' is not defined
>>> a.keys()
dict_keys([7, 89, 'puyhon'])
