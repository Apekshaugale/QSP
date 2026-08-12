#wap to check guve number is armstrong number or not
a=153
total=0
b=str(a)#153--->'153'
print(b)#---->iterable
power=len(b)
print(power)
for i in b:
    total=total+int(i)**power
    print('total =',total)
if total==a:
    print('Its a armstromg number')
else:
    print('Its not a armstromg number')
'''
