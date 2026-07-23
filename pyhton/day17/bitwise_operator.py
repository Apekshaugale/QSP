Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#bitwise operator

#which will perform bit by bit operation.

#only work on interger data type

#bitwise and (&)

#1 1---1

19&13
1

24 & 17
16

54 & 32
32

47&37
37

24 & 19
16

16 &8
0


#bitwise or(!)
#bitwise xor(^)


#bitwise or(!)
#it will convert given integer number into binary digit and perform bit by bit

#syntax----> op1 |op
#syntax----> op1 |op2

~556
-557

~-50
49

~50
-51

bin()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    bin()
TypeError: bin() takes exactly one argument (0 given)
bin(11)
'0b1011'

>>> 11>>3
1
>>> 
>>> 11<<3
88
>>> 
>>> 17<<3
136
>>> bin(17)
'0b10001'
>>> 
>>> bin(136)
'0b10001000'
>>> 
>>> 17>>3
2
>>> 
>>> bin(2)
'0b10'
>>> 
>>> 
>>> #bitwise left sift(<<)
>>> #bitwise right shift(>>)
>>> #syntax--->op1<<n
>>> #where, n is integier.
>>> 18<<n
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    18<<n
NameError: name 'n' is not defined
