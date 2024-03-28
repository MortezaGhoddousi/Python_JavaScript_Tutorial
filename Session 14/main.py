
def sayHello():
    print('Hello dude')


print("Start the script!")
sayHello()

def sumNums (x, y):
    z = x+y
    print(z)
    return z

z = sumNums(4, 9)
print(z)

myInfo = ['Morteza', 'Ghoddousi', 29, 'Male', 1.86, 91]

print(myInfo[0])

myInfo.append('Black')

print(myInfo)

print(len(myInfo))

yourInfo = ["AmirReza", "Shirdel", 26, "Male", 1.79, 105]
print(yourInfo)

# [1, 4, 7]
# [1, 8, 4, 9, 12]
def calAvg(inp):
    sum = 0
    for i in inp:
        sum = sum+i
    return sum/len(inp)


avg = calAvg([1, 4, 7])
print(avg)

avg = calAvg([1, 8, 4, 9, 12])
print(avg)
