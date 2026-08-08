'''

&#x20;                   **#enumerate**



s="Hello"  #-----> 0-->H

"""

normal syntax :--->

&#x20;        

&#x20;   enumerate(iterable)--->inbuilt function

&#x20;        |

&#x20;        |

&#x20;   Data will convert To object address

&#x20;        |

&#x20;        |

&#x20;   Object Address Data again convert To readable format

&#x20;        |

&#x20;        |

&#x20;   Two ways---->1 -->Typecasting   2--->Looping

&#x20;        |

&#x20;        |

&#x20;   syntax for Typecasting

&#x20;   

&#x20;   list(enumerate(iterable))

&#x20;   tuple(enumerate(iterable))

&#x20;   dict(enumerate(iterable))

&#x20;   set(enumerate(iterable))

&#x20;       |

&#x20;       |

&#x20;   syntax for---> Looping

&#x20;   

&#x20;   for variable in enumerate(iterable):

&#x20;       statement

&#x20;        

&#x20;        |

&#x20;        |

&#x20;  output of enumerate function----->(Position,value)

"""

s="Hello"

print(enumerate(s)) #<enumerate object at 0x000002201988D530>



\#way---->1  Typecasting

print(list(enumerate(s)))

\#\[(0, 'H'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]



print(tuple(enumerate(s)))

\#((0, 'H'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o'))



print(set(enumerate(s)))

\#{(4, 'o'), (0, 'H'), (2, 'l'), (1, 'e'), (3, 'l')}



print(dict(enumerate(s)))

\#{0: 'H', 1: 'e', 2: 'l', 3: 'l', 4: 'o'}



\#way--->2

for i in enumerate(s):

&#x20;   print(i)

"""

(0, 'H')

(1, 'e')

(2, 'l')

(3, 'l')

(4, 'o')



"""

for i,j in enumerate(s):

&#x20;   print(i,j)

"""

i----->Position

j----->value



Note :--> when we use two reference\_variable

&#x20;         Here will get output in unpacked format

&#x20;         

"""



\# k=\[10,20,30,40,50]



y={1:2,4:5,8:9}

for i in enumerate(y):

&#x20;   print(i)

'''

















"""

\*.**reversed-**------> inbuilt function



\*.In reversed if we done operation directly it will

&#x20; show object address



\*.In reversed To avoid object addressdata we have

&#x20; two ways 

&#x20; 1.Typecasting

&#x20; 2.Looping



&#x20;   Typecasting syntax :--->

\--------------------------------------------------

&#x20;   list(reversed(iterable))

&#x20;   tuple(reversed(iterable))

&#x20;   dict(reversed(iterable))

&#x20;   set(reversed(iterable))



&#x20;       Looping syntax :--->

\-----------------------------------------------

&#x20;   for variable in reversed(iterable):

&#x20;       statement 

"""



s="Python"

'''

Typecasting

print(reversed(s)) #<reversed object at 0x00000252911A1420>

print()

print(list(reversed(s)))

\#\['n', 'o', 'h', 't', 'y', 'P']

print(tuple(reversed(s)))

\#('n', 'o', 'h', 't', 'y', 'P')

print(set(reversed(s)))

\#{'o', 'n', 'h', 'P', 'y', 't'}

print(dict(reversed(s))) #ValueError

'''

'''

s="Python"

for i in reversed(s):  #inbuilt function

&#x20;   print(i,end=" ")

print()

for i in s\[::-1]:   #slicing

&#x20;   print(i,end=" ")

print()

s="Python"

for i in range(-1,-len(s)-1,-1):#range()

&#x20;   print(s\[i],end=" ")

print()



s="Python"

res=" "

for i in s:

&#x20;   res=i+res

print(res)

'''

'''

d=\[1,2,3,4,5]



for i in reversed(d):

&#x20;   print(i,end=" ")

print()

for i in d\[::-1]:

&#x20;   print(i,end=" ")

print()



for i in range(-1,-len(d)-1,-1):

&#x20;   print(d\[i],end=" ")



d=\[1,2,3,4,5]

l=\[]

for i in d:

&#x20;   l=\[i]+l

print(l)

'''

'''

\#26.wap to check how many words are present

\# in the given sentence

a="hello world sentence"

b=a.split()

print(b) #\['hello', 'world', 'sentence']

total=0

for i in b:

&#x20;   total=total+1

print(total)

'''













'''

\# 27.wap to create a dictionary and print the characters

\# and its Ascii value pair

s="hello world"

\# output:--> {"h":ascii value,"e":ascii value........}

d={}

for i in s:

&#x20;   d.update({i:ord(i)})

print(d)



d={}

for i in s:

&#x20;   d\[i]=ord(i)

print(d)

'''

'''

\# 28.wap to create a dictionary and

\# traverse into it and if the length is

\# even print as it else reverse it

names=\["apple","google","yahoo","microsoft","gmail","walmart"]

\# output:-->{'apple': 'elppa', 'google': 'google', 'yahoo': 'oohay', 'microsoft': 'tfosorcim', 'gmail': 'liamg', 'walmart': 'tramlaw'}

d={}

for i in names:

&#x20;   if len(i)%2==0:

&#x20;       d\[i]=i

&#x20;   else:

&#x20;       d\[i]=i\[::-1]

print(d)

'''

\# 29.wap to print series of factorial(take user input)

num=eval(input("enter the Number"))

fact=1

for i in range(1,num+1,1):

&#x20;   fact=fact\*i

&#x20;   print(i)

print(fact)

"""

fact=1

i=1

fact=fact\*i----> fact=1\*1----=1

i=2

fact=fact\*i----> fact=1\*2----=2



i=3

fact=fact\*i----->fact=2\*3----=6



i=4

fact=fact\*i---> fact=6\*4----=24



i=5

fact=fact\*i---> fact=24\*5---=120

