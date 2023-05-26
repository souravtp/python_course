"""
The one-parameter variant of the center() method makes a copy of the original string,trying to center it inside
a field of a specified width.
The centering is actually done by adding some spaces before and after the string.
If the target field's length is too small to fit the string, the original string is returned.

The two-parameter variant of center() makes use of the character from the second argument, instead of a space.
"""

print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')

print('[' + 'gamma'.center(11, '*') + ']')
print('[' + 'delta'.center(15, '*') + ']')


"""The endswith() method checks if the given string ends with the specified argument and returns True or False"""

t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))
