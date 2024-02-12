# # Example 2

# weight = float(input('Enter your weight: '))
# height = float(input('Enter your height: '))


# if height < 3:
#     height = height*100

# print(f'Your weight is: {weight}')
# print(f'Your height is: {height}')
# BMI_Index = weight/(height**2)*(10**4)

# print(f'Your BMI index is: {BMI_Index}')

# Example 1

import random

choices = ['rock', 'scissors', 'paper']

napar = True
nappar = True

while napar:
    if nappar:
        userChoice = input('Enter your choice: (rock, scissors, paper)') 
        computerChoice = random.choice(choices)

        userChoice = userChoice.lower()
        if not (userChoice == 'rock' or userChoice == 'scissors' or userChoice == 'paper'):
            print('invalid input')
        else:
            print(f'Your choice is {userChoice}')
            print(f'Computer choice is {computerChoice}')
            if userChoice == computerChoice:
                print('Draw!')
            else:
                if userChoice == 'rock':
                    if computerChoice == 'paper':
                        print('Computer Won!')
                    elif computerChoice == 'scissors':
                        print('User Won!')
                if userChoice == 'paper':
                    if computerChoice == 'scissors':
                        print('Computer Won!')
                    elif computerChoice == 'rock':
                        print('User Won!')
                if userChoice == 'scissors':
                    if computerChoice == 'rock':
                        print('Computer Won!')
                    elif computerChoice == 'paper':
                        print('User Won!')
        
    checkContinue = input('Do you want to play again? (y/n)')
    checkContinue = checkContinue.lower()
    
    if checkContinue == 'y':
        napar = True
        nappar = True
    elif checkContinue == 'n':
        napar = False
        nappar = False
    else:
        print('invalid input')
        nappar = False
        
        
                
                



