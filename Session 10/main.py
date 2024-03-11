AmirRezaInformation = ['AmirReza', 'Shirdel', 25, 'Developer', 105.8, 1.79]

print(AmirRezaInformation)

print(f'The weight of {AmirRezaInformation[0]} {AmirRezaInformation[1]} is: {AmirRezaInformation[4]} kg')


numStu = int(input('Enter the number of your students: '))

scores = []
sum = 0

minScore = 21
maxScore = -1

for i in range(numStu):
    s = float(input(f'Enter {i+1}th score: '))
    scores.append(s)
    sum = sum+scores[-1]

    if scores[-1] > maxScore:
        maxScore = scores[-1]
    if scores[-1] < minScore:
        minScore = scores[-1]

    # print(scores[0])
    # print(scores[-1])
    # print(scores[i])
print(scores[0])
print(scores[-1])


avg = sum/numStu
print(f'The average of students is: {avg}')
print(f'The minimum of scores is: {minScore}')
print(f'The maximum of scores is: {maxScore}')


import numpy as np

print(np.average(scores))
print(np.min(scores))
print(np.max(scores))

print(scores)
scores.insert(1, 'amirreza')
print(scores)

scores.pop(1)
print(scores)

i = scores.index(13)
print(i)

scores.pop(i)
print(scores)

scores.pop(scores.index(20))