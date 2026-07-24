Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Print()statement-->
#to display output in python [on screen]we use print().
>>> #syntax--->print(val1,val2,.....valn,end='\n',sep='')
>>> #    by default seperator will take space as value.
>>> #    by default end will take next line as value.
>>> 
>>> print(5,67,87,54)
5 67 87 54
>>> print(5,67,87,54,sep='hiii')
5hiii67hiii87hiii54
>>> 
>>> print('manoj is good boy',end=' ')
manoj is good boy 
>>> print('manoj is good boy',end='')
manoj is good boy
>>> 
>>> print('karma dharma')
karma dharma
>>> 
>>> print(5,67,87,54,sep='@')
5@67@87@54
>>> 
>>> a='hello'
>>> print('manoj is good boy',end='a')
manoj is good boya
>>> print('manoj is good boy',end=(a))
manoj is good boyhello
>>> print('manoj is good boy',end=(\na))
SyntaxError: unexpected character after line continuation character
>>> print('manoj is good boy',\n end=(a))
SyntaxError: unexpected character after line continuation character
>>> 
