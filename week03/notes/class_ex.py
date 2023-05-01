"""
Examples from the start of class on 05.01.2023
Working with slicing, splitting, and joining lists/dictionaries
"""

names = ['John', 'Bob', 'Jenny']
# how to log this?
s = str(names)
print(s[1:-1].replace("'", ""))

words = 'the cat is big'.split()
print(words)
print(' '.join(words))
print(' - '.join(words))
print(' '.join(names))