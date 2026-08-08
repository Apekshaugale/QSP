'''enumerate

enumerate is te inbuild function.

it is used to print both position and character .

syntax====>

enumerate (iterable)

'''

#enumerate -->  inbuils function  --> object address---> to convert redable format used typescasting or looping.

'''normal syntax:
                                    enumertae(iterable)------>inbuild function
                                               |

                                               |
                                Data will converted to object address
                                              |
                                              |
                            Object address data again converted into
                                              |
                                              |
               Two ways--1.TYpecasting  or 2.looping
                                             |
                                             |
                    Syntax for typecasting

                      list(enumerate(iterable))
                      tuple(enumerate(iterable))
                      set(enumerate(iterable))
                      dict(enumerate(iterable))'''

                    #synatax for looping
'''
                       for variable in enumerate(iterable):
                                   statement
                                          |
                                          |
                    output of enumerate function in form of tuple --->(position,value)
                    '''

s='hello'
print(enumerate(s))#object addresss
print(list(enumerate(s)))
print(tuple(enumerate(s)))
print(set(enumerate(s)))
print(dict(enumerate(s)))

#using looping syntax
for a in enumerate(s):
        print(a)



for a,b in enumerate(s):
        print(a)

'''
a--->postion (first always pointing to )
b--->value/character (second always pointing to )

output always unpacked when we used one referance variable output will packed'''

#wap to print character as well as postion
k=[10,20,30,40,50]
print(list(enumerate(k)))


for a,b in enumerate(k):
        print(a)


        
