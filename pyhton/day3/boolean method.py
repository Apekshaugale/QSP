Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
c='idshjl'
c.isalpha()
True

d='FGUGHDKJL'
d.isaplha()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    d.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
d.isalpha()
True

 

#isalnum()
#here we can use only alphabet and numbers.you can use only numbers or alphabets.
#not special charcters are allowed you will get false as output.
#syntax-->varname.isalnum()

a='wqhihlfj23'
a.isalnum()
True

b='hio232#'
b.isalnum()
False
False
False


#isdigit()
#syntax:  varnam.isdigit()
#no alphabets,no special charcters -->false output
#only numbers and numbers persent in "" quotes.
#without quotes it will show attributes error.
s=2244
s.isdigit()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
s='2390'
s.isdigit()
True

#isupper()


#alphabets are manditory,numbers and special charactres are optional.
a='HIDFOPI;'
a.isupper()
True

a='2000'
a.isupper()
False


#islower()
#only lower case alphabtes are manditory
a='jojpfs3980:"'
a.islower()
True

a='o3740'
a.islower()
True

a='097-94'
a.islower()
False

a='gkjl'
a.islower()
True

a='ADYGJ302'
a.islower()
False

a='^*))_'
a.islower()
False

#uppercase,only number,special cahracters gives output as false
a='58#$$assDFDGF'
a.islower()
False
#uppercase are not allowed


#istitle()
#syntax-->varname.istitle()

s='Hi hello'
s.istitle()
False

s.title()
'Hi Hello'

s
'Hi hello'

s='nlkv ekdfjo'
s.istitle()
False


#issapce()
#syntax-->varname.isspace()
s=''
s.isspace()
False

s=' '
s.isspace()
True

#it will give output as true when only tab space is given .
s='    fihojl'
s.isspace()
False
False
False

s3='   Hi'
s3.isspace()
False
s='ojk  eioufo'
s.isspace()
False



#stratswitch()
#syntax-->varname.startswith('substing',startindex)

y='python class is done'
y.startswith('python')
True

y.startswith('ython')
False

y.startswith('hon')
False
y.startswith('ython',1)
True

y.startswith('hon',3)
True
y.startswith('done')
False
y.startswith('done',16)
True



#endswith()
#syntax-->varname.endswith('substring',startindex,endindex+1)
go with possitive value
SyntaxError: invalid syntax

w='python class done'
w.endswith('done')
True

w.endswith('e')
True
w.endswith('class')
False
w.endswith('class',7,12)
True


e='walmart snapchat instagram dataload'
e.startswith('snapchat',8)
True
>>> e.startswith('snapchat')
False
>>> 
>>> e.startswith('walmat')
False
>>> 
>>> #if given name is not present then it will give output as false
>>> 
>>> e.endswith('snapchat')
False
>>> e.endswith('snapchat',8,16)
True
>>> e.endswith('dataload')
True
>>> e.startswith('snapchat')
False
>>> e.startswith('dataload',27,35)
True
>>> e.startswith('dataload',27)
True
>>> 
>>> #Booolean methods
>>> #1.isalpha()
>>> #2.isalnum()
>>> #3.isdigit()
>>> #4,istitle()
>>> #5.isspace()
>>> #6.isupper()
>>> #7.islower()
>>> #8.startswith()
>>> #9.endswith()
