import numpy as np

x = 15
y = 6
print(x/y)
print(x//y)
print(np.mod(x, y))

x = x+1

print(True and False)

age = 19

if age > 18:
    print('Adult')
elif age < 10:
    print('Child')
else: 
    print('Teenager')