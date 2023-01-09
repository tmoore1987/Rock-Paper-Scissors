import random

#rules of the game
print(f'Winning Rules of Rock, Paper, Scissors: \n' 
'Rock vs. Paper -> Paper wins \n' 'Rock vs. Scissors -> Rock wins \n' 'Paper vs. Scissors -> Scissors wins')

playing = True

while playing:
    print(f'Enter choice of \n 1 for Rock, \n 2 for Paper, and \n 3 for Scissors.' )
    
    #input from user
    choice = int(input(f' User turn: '))
   
    # must loop until there is a valid choice
    while choice > 3 or choice <1:
        choice = int(input(f' Enter valid choice: '))

    if choice ==1:
        choice_name = 'Rock'
    elif choice ==2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    print(f' User choice is {choice_name}.')

    #computer must choose

    print(f' Computer must enter choice of  \n 1 for Rock, \n 2 for Paper, and \n 3 for Scissors. ')
    #enter computer choice
    comp_choice = random.randint(1,3)

    if comp_choice ==1:
        choice_name = 'Rock'
    elif comp_choice ==2:
        choice_name = 'Paper'
    else:
       choice_name = 'Scissors'

    print(f' Computer choice is {choice_name}.')

    if choice ==comp_choice:
        print(f'Draw. ', end = ' \n')

    elif choice == 1 and comp_choice == 2 or choice ==2 and comp_choice ==1:
        print(f'Paper wins! ', end=' \n')
    elif choice ==1 and comp_choice ==3 or choice ==3 and comp_choice== 1:
        print(f'Rock wins! ', end= ' \n')
    else:
        print(f'Scissors wins! ', end= ' \n')

    #play again function
    restart = input("Play again? (y/n): ").lower()
    if not restart == 'y':
        playing = False

print('Thanks for playing!')
    
    
        






