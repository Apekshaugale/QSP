'''
34.wap to create a dictionary index and word pair
s="tomorrow is weekend and non-veg special"
o/p:-->{0: 'tomorrow', 1: 'is', 2: 'weekend', 3: 'and', 4: 'non-veg', 5: 'special'}


s="tomorrow is weekend and non-veg special"
d={}
for i,j in enumerate(s.split()):
    d[i]=j
print(d)


35.wap to create a dictionary words and its length pair
s="tomorrow is weekend and non-veg special"

o/p:-->{'tomorrow': 8, 'is': 2, 'weekend': 7, 'and': 3, 'non-veg': 7, 'special': 7}


s="tomorrow is weekend and non-veg special"
d={}
for i ,j  in enumerate(s.split()):
    d[j]=(len(j))
print(d)



36.wap to create a dictionary characters and its corresponding upper case characters
s="sunday"
o/p:-->{'s': 'S', 'u': 'U', 'n': 'N', 'd': 'D', 'a': 'A', 'y': 'Y'}
s="sunday"
d={}
for i in s:
    d[i]=i.upper()
print(d)
   

37.wap to create a dictionary Ascii and character pair
l=[89,51,111,77,108,120]

o/p:-->{89: 'Y', 51: '3', 111: 'o', 77: 'M', 108: 'l', 120: 'x'}


l=[89,51,111,77,108,120]
d={}
for i in l:
    d[i]=chr(i)
print(d)
'''
'''
38.wap to  create a list of characters and its Ascii value pair
s="sunday"
o/p:-->[('s', 115), ('u', 117), ('n', 110), ('d', 100), ('a', 97), ('y', 121)]'''



s = "sunday"
l = []

for i in s:
    l.append((i, ord(i)))

print(l)



