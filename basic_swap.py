#!/usr/bin/python
a = 1
b = 2
print(f'Initial a={a}, b={b}')

# swap using temporary variable
tmp = a
a = b
b = tmp

del tmp

print(f'Now a={a}, b={b}')

# swap using math (only work for data-type number)
a = a + b
b = a - b
a = a - b

print(f'Now a={a}, b={b}')

# just swap (Python style)
a, b = b, a

print(f'Now a={a}, b={b}')
