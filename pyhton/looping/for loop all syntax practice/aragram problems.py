5.WAP to check whether string is ANAGRAM or not
#sorted will work on ascii charcter it will work always asc to desc .written type is list.
#anagrams : characters should be same it can different meaning
#tea, eat
#silent, listen
#bored , robed
#cat, act
#keep, peek
#lamp, palm
"""
"""
a= 'tea'
b='eat'
print(sorted(a))
print(sorted(b))
if sorted(a)==sorted(b):
    print('its a anagram')
else:
    print('its not  anagram')

a= 'tea'
b='ate'
print(sorted(a))
print(sorted(b))
if sorted(a)==sorted(b):
    print('its a anagram')
else:
    print('its not  anagram') 


#silent, listen
a='silent'
b='listen'
if sorted(a)==sorted(b):
   print('its a anagram')
else:
    print('its not  anagram') 

#bored , robed
a='bored'
b='robed'
if sorted(a)==sorted(b):
    print('Its a anagram')
else:
    print('Its not a anagram')


#cat, act

a='cat'
b='act'
if sorted(a)==sorted(b):
    print('Its a anagram')
else:
    print('Its not a anagram')

    
#keep, peek
a='keep'
b='peek'
if sorted(a)==sorted(b):
    print('Its a anagram')
else:
    print('Its not a anagram')

    
#lamp, palm
a='lamp'
b='palm
if sorted(a)==sorted(b):
    print('Its a anagram')
else:
    print('Its not a anagram')
