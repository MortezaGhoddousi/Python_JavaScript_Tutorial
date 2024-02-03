# admin = '123'

# guess = (input('enter your password: '))

# while guess != admin:
#     print('Password is wrong')
#     print('Try again')
#     guess = (input('enter your password: '))
    
# print('access granted')
    
    
x = [0, 0, 0]

for i in range(3):
    x[i] = int(input('enter your score: '))
    
print(x)
    
i = 0

min = 21
max = -1
sum = 0
while i < 3:
    if x[i] < min:
        min = x[i]
    if x[i] > max:
        max = x[i]
    sum = sum+x[i]
    i = i+1
print(min)
print(max)
print(sum/3)
