#77.  Write a program to check if the last element in a list is even. (e.g., l = [1, 2, 4])#l[-1]%2==0

list=eval(input('Enter the element: '))
if list[-1]%2==0:
    print(f'The last number "{list[-1]}" is even.')
