# for i in range(3):
#     grade = int(input(f"enter u {i+1} grade ="))
#     if grade >= 10 :
#         print("passed")
#     else:     
#         print("faild")

# i= 0 
# while i<3:
#     x= int(input(f"enter u {i+1} grade = "))
#     if x >= 10:
#         print("passed")
#     else:
#         print("faild")
#     i = i + 1

import numpy 

i = 0
while i <= 20:
    if i<10:
        print(i)
    elif not numpy.mod(i,2)==0:
        if not i == 13:
            print(i)
    i= i + 1


        
        


