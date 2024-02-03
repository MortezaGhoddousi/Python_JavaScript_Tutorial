x = 'morteza'
y = 2
z = 3.5
h = True

print(type(x))
print(type(y))
print(type(z))
print(type(h))

inp = input('Enter your score: ')
inp = int(inp)
inp = float(inp)
print(type(inp))

y = str(y)
print(type(y))
print(y)

j = 5/2
print(j, type(j))

print(4/2, type(4/2))

print(2+3.0)

distance = 14
unit = 'km'
print(str(distance)+unit)

print(f"the distance is: {distance}")

# Comparison operators
print('================================================')
print ('Comparison operators ')

x = 10
y = 12

print(f'{x} < {y} = ', x < y) # lower than
print(f'{x} <= {y} = ', x <= y) # lower than or equal to
print(f'{x} > {y} = ', x > y) # greater than
print(f'{x} >= {y} = ', x >= y) # greater than or equal to
print(f'{x} == {y} = ', x == y) # equal to
print(f'{x} != {y} = ', x != y) # not equal to

# Logical operators 
print('================================================')
print ('Logical operators ')
print(f"{True} and {False} = ", True and False)
print(f"{True} and {True} = ", True and True)
print(f"{False} and {False} = ", False and False)
print(f"{False} and {True} = ", False and True)
print(f"{True} or {False} = ", True or False)
print(f"{False} or {True} = ", False or True)
print(f"{True} or {True} = ", True or True)
print(f"{False} or {False} = ", False or False)

