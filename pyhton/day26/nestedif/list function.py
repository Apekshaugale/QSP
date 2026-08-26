ls=eval(input('Enter the list data : '))
if type(ls)==list:
   print('1.pop()') 
   print('2.append()') 
   print('3.clear()')
   choice=int(input('Enter the choice : '))
   if choice==1:
      ls.pop()
      print(ls)
   else:
      if choice==2:
         data=input('ENter the data : ')
         ls.append(data)
         print(ls)
      else:
         if choice==3:
            ls.clear()
            print(ls)
         else:
            print('Invalid choice .')
else:
   print('Enter data is not a list ')
         