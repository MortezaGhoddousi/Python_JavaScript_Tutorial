# # Exercise 1

# a = float(input('Enter a Coef: '))
# b = float(input('Enter b Coef: '))
# c = float(input('Enter c Coef: '))

# delta = b**2 - 4*a*c

# if delta < 0:
#     print('There is no root')
# elif delta == 0:
#     x = (-b) / (2*a)
#     print(f'The root of equation is: {x}')
# else:
#     x1 = (-b + delta) / (2*a)
#     x2 = (-b - delta) / (2*a)
#     print(f'The roots of equation are: {x1} and {x2}')
    

# Exercise 2

# admin = ''
try:
    fileRead = open('./passwords.txt')
    for line in fileRead.readlines():
        admin = line
except:
    admin = ''

while True:
    option = input('Enter your choice (1: for set a password, 2: for change a password, 3: for enter to your profile): ')
    if option == '1':
        if admin == '':
            admin = input('Enter your password: ')
            myFile = open('./passwords.txt', 'w')
            myFile.write(admin)
            myFile.close()
        else:
            print('Password has been set! In order to change the password choose correct option!')
    elif option == '2':
        oldpass = input('Enter your password: ')
        if oldpass == admin:
            pass1 = input('Enter your new password: ')
            pass2 = input('Enter your new password again: ')
            if pass1 == pass2:
                admin = pass1
                myFile = open('./passwords.txt', 'w')
                myFile.write(admin)
                myFile.close()
                print('Password has been changed!')
            else:
                print("Your confirm password must be matched!")
        else:
            print('Wrong password!')
    elif option == '3':
        guess = input('Enter your password: ')
        if guess == admin:
            print('Access Granted!')
            break
        else:
            print('Wrong password!')

# myFile = open('./passwords.txt', 'a')
# # print(myFile)
# myFile.write('My new password is: 111 \n')

# fileRead = open('./passwords.txt')

# for line in fileRead.readlines():
#     print(line) 


# myFile.close()