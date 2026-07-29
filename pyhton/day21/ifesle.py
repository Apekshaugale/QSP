#wop to check the given data type is string
a=eval(input('Enetr the data :'))
if type(a)==str:
    print('string data type')

#wop to check given data type is sequence data type or not
x=eval(input("Enter the data type :"))
if type(x)in (str,list,tuple):
    print("the sequrnce data type")

 #or using isinstance()--->syntax:(vn,(datatype1,dt2,dt3))
x=eval(input("Enter the data type :"))
if isinstance(x,(str,list,tuple)):
    print("the sequrnce data type")    
