def factorial(n):
    a = 1
    x = 1
    while (a < n):
        x = x * a
        a = a+1
    
    return x


x = factorial(5)
print("The value of 5! is: ", x)
