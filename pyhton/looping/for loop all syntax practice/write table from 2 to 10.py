#wap to write a table from2 to 10 numbers
for i in range(1,11):
    for j in range(2,11):
        print(i*j,end=' ')
    print()


for i in range(1,11):
    for j in range(1,11):
        print(f'{i}*{j}----> {i*j}')
    print()
