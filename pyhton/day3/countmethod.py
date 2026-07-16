Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#count()
#syntax:vn.count('substring',startindex,endindex+1).
#where start index and end index are optional.

y='Goood Morning'
#in a given sring what caharcter we are passing and how many character are repeated
y.count('Good')
0

y.count('d')
1

y.count('o')
4

y.count('O')
0

y.count('D')
0

#if caharcter is not present which is passed then we will not present then we will get output as zero

r='Python class and Morning session'

 
r.count('o')
3

r.count('o',5)
2

r.count('o',5,20)
1

>>> r.count('P',5,20)
0
>>> 
>>> r.count('g',5,27)
1
>>> r.count('s',5,20)
2
>>> 
>>> r.count('s')
5
>>> 
>>> r.count('s',21,25)
0
>>> 
>>> KeyboardInterrupt
>>> r.count('')
33
>>> d='Hello'
>>> d.count('')
6
>>> #whenever we are working with count method it will take spaces after every charcter by default._H_E_L_L_O_
>>> #if i giving empty spaces it will count zero eg.e.count(''):o/p-->0
>>> 
>>> 
>>> y
'Goood Morning'
>>> #write a program to check how many times widespaces are present also uppercase ,lowercase how many times are present.
>>> 
>>> 
>>> 
