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
