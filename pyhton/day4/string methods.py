Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="Good Morning"
"*".join(a)
'G*o*o*d* *M*o*r*n*i*n*g'

b="Hello"
"123".join(b)
'H123e123l123l123o'

c="Master"
"-".join(c)
'M-a-s-t-e-r'

l=["abc","xyz","mno"]
str(l)
"['abc', 'xyz', 'mno']"

l
['abc', 'xyz', 'mno']

"".join(l)
'abcxyzmno'

" ".join(l)
'abc xyz mno'

"--".join(l)
'abc--xyz--mno'



s=("Ram","sham","rahul")

"".join(s)
'Ramshamrahul'

",".join(s)
'Ram,sham,rahul'


#join()

#syntax :--> "joining_character".join(iterable)






#join()
#syntax :--> "joining_character".join(iterable)


a="xyz"
"7".join(a)
'x7y7z'


b="Morning"
"*".join(b)
'M*o*r*n*i*n*g'


c=["Hello","python","java"]

"".join(c)
'Hellopythonjava'

" ".join(c)
'Hello python java'

"---".join(c)
'Hello---python---java'


k=("walmart","join","upper")

"".join(k)
'walmartjoinupper'

"   ".join(k)
'walmart   join   upper'


t={"abcd","xyzmno","wert"}

"".join(t)
'xyzmnowertabcd'

"--".join(t)
'xyzmno--wert--abcd'


w={"abc":"xyz","hello":"Hii","get":"key"}
"".join(w)
'abchelloget'

" ".join(w)
'abc hello get'




a=" Hello "
a.split()
['Hello']

a=" Hello "
a.split(" ")
['', 'Hello', '']

a
' Hello '

.split("l")
SyntaxError: invalid syntax


a.split("l")
[' He', '', 'o ']




t="Goodmorning"
t.split()
['Goodmorning']

t.split("Good")
['', 'morning']

t
'Goodmorning'

t.split("o")
['G', '', 'dm', 'rning']

t.split("o",1)
['G', 'odmorning']

t.split("o",2)
['G', '', 'dmorning']



t
'Goodmorning'

t.split("o")
['G', '', 'dm', 'rning']

t.rsplit("o")
['G', '', 'dm', 'rning']


t.split("o",1)
['G', 'odmorning']

t.rsplit("o",1)
['Goodm', 'rning']



s="Rahul kiran mahii rohit sachin"

s.split()
['Rahul', 'kiran', 'mahii', 'rohit', 'sachin']

s="Rahulkiranmahiirohitsachin"
s.split()
['Rahulkiranmahiirohitsachin']

s="Rahul kiran mahii rohit sachin"

s="Rahul kiranmahii rohitsachin"
s.split()
['Rahul', 'kiranmahii', 'rohitsachin']






#split()-----> var_name.split(separater,maxsplit)

s="Python"
s.split()
['Python']

s1="Hi Hello Python"
s1.split()
['Hi', 'Hello', 'Python']

s2="Programming class"
s2.split("ram")
['Prog', 'ming class']

s2
'Programming class'

s2.split("m")
['Progra', '', 'ing class']

s2.split("m",1)
['Progra', 'ming class']

s2.rsplit("m",1)
['Program', 'ing class']

s3.split("Class")
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    s3.split("Class")
NameError: name 's3' is not defined. Did you mean: 's'?
s2.split("Class")
['Programming class']

s2
'Programming class'

s2.split()
['Programming', 'class']





s="Python"
s.removeprefix("P")
'ython'

s.removeprefix("t")
'Python'

s.removeprefix("Pyt")
'hon'



s2
'Programming class'

s2.removeprefix("Progr")
'amming class'

s2.removeprefix("r")
'Programming class'


s2
'Programming class'

s2.removesuffix("s")
'Programming clas'

s2.removesuffix("lass")
'Programming c'

s2.removesuffix("ssal")
'Programming class'




s2
'Programming class'

s2.removesuffix("ing class")
'Programm'


s2
'Programming class'

s2.removesuffix("ingclass")
'Programming class'




x="GoodMorning"
x.index("M")
4

x.index("Good")
0

x.index("o")
1

x.index("o",2)
2

x.index("o",3)
5

x.index("o",31)
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    x.index("o",31)
ValueError: substring not found


x
'GoodMorning'

x.index("g")
10

x.index("n")
7

x.index("n",8)
9

x.index("Mor")
4

x.index("Python")
Traceback (most recent call last):
  File "<pyshell#226>", line 1, in <module>
    x.index("Python")
ValueError: substring not found




y="welcome to all"
y.index(" ")
7
y.index(" ",8)
10

y.index("l")
2

y.index("l",3)
12

y.index("come")
3




x
'GoodMorning'


x.index("n")
7

x.rindex("n")
9


x.index("n",8)
9

x.rindex("n",8)
9

x.rindex("n",0,8)
7

x
'GoodMorning'

x.index("o")
1

x.rindex("o")
5

x.index("o",3)
5

x.rindex("o",0,2)
1



t="First class first Marks first day"

t.index("a")
8

t.rindex("a")
31

t.rindex("a",0,10)
8


x
'GoodMorning'


x.index("G")
0

x.find("G")
0

x.index("o")
1

x.find("o")
1

x.index('o',3)
5

x.find('o',3)
5

x.index("l")
Traceback (most recent call last):
  File "<pyshell#290>", line 1, in <module>
    x.index("l")
ValueError: substring not found

x.find("l")
-1


x
'GoodMorning'

x.rindex("n")
9

x.rfind("n")
9

x.rindex("n",0,8)
7

x.rfind("n",0,8)
7

x.rindex("k")
Traceback (most recent call last):
  File "<pyshell#305>", line 1, in <module>
    x.rindex("k")
ValueError: substring not found

x.rfind("k")
-1

x.rfind("king")
-1




s="     Hii      "

s.strip()
'Hii'

s
'     Hii      '

s.strip(" ")
'Hii'



k
('walmart', 'join', 'upper')

e="@#Hello@#"


e.strip("@")
'#Hello@#'

e
'@#Hello@#'

e.strip("#")
'@#Hello@'

e.strip("Hello")
'@#Hello@#'

e
'@#Hello@#'
e.strip("H")
'@#Hello@#'


t="Python"
t.strip("P")
'ython'

t.strip("n")
'Pytho'

t.strip("y")
'Python'

t.strip("Pyt")
'hon'

e
'@#Hello@#'


r="@#$Hi@#$"

r.strip("@")
'#$Hi@#$'

r.strip("#")
'@#$Hi@#$'

r.strip("Hi")
'@#$Hi@#$'

r.strip("@#$")
'Hi'



r
'@#$Hi@#$'

r.strip("@#$")
'Hi'

r.lstrip("@#$")
'Hi@#$'

r.rstrip("@#$")
'@#$Hi'
