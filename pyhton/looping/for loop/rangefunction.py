'''range(SE,EN,SV)----->
startpoint,endpoint,stepvalue

if we pass only on eargument it will consoider as a endindex.By default it will take Start index as 0 and stepvalue is 1'''
'''

for i in range(10):
    print(i,end=' ')
print()
     
#wap to print 15 to 30
for i in range(15,31):
    print(i,end=' ')
print()
    
#wap to print 10 to 20 in between even numbers
for i in range(10,21,1):
    if i%2==0:
      print(i,end='  ')
print()

#or

for i in range(10,21,2):
      print(i,end=" ")
print()
'''
'''
#print from 10 to 1
for i in range(10,0,-1):
      print(i,end=" ")
print()


#print from 50 to 35
for i in range(50,34,-1):
      print(i,end=" ")
print()



#print postion of caharcter in string

s='PYTHON'
for i in range(len(s)):
      print(i,s[i])  #indexing--vn[postion]
print()

s=['Morining','Walmart','hello','joy','Part']
for i in range(len(s)):
    print(i,'---->',s[i])
'''

#Wap  to print sum of number from 0to 10
Total=0  #always print this varible outside the for loop'''
for i in range(0,11,1):
    Total=Total+i
    print(Total)#it will ive output in iteration so we want it to ptint outside for loop
print(Total)

#print all element and its ascii value
s='Hello'
x={}
for i in s:          
    x[i]=ord(i)  #vn[key]=value
    x.update({i:ord(i)})  #vn.update({key:value})
print(x)

'''print count of uppercase caracter'''
s='PyTHOn'
char=0
for i in s:
    if i.isupper():
        char=char+1
print(char)

