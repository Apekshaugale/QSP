'''Print only alphabets.
s = "Python123Java456"
for a in s:
    if a.isalpha():
        print(a,end=' ')


        '''

'''Print only uppercase letters.
s = "PyTHonJAVA"
for c in s:
    if c.isupper():
        print(c)
    
'''


'''
Print words having even length.
'''
l = ["python", "sql", "java", "html", "css"]
for a in l:
    if len(a)%2==0:
        print(a)
'''odd lenth '''
l = ["python", "sql", "java", "html", "css"]
for a in l:        
   if len(a)%2==1:
       print(a)

'''Print all keys.'''

d = {101: "Ram", 102: "Shyam", 103: "Amit"}
for a in d:
    print(a)


d = {101: "Ram", 102: "Shyam", 103: "Amit"}
for a in d.keys():
    print(a)

'''Print all values.'''

d = {101: "Ram", 102: "Shyam", 103: "Amit"}
for a in d.values():
    print(a)

d = {101: "Ram", 102: "Shyam", 103: "Amit"}
for a in d.items():
    print(a)
