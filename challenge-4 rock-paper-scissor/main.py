import random

user_input = int(input('what do you choose : type 0 for Rock, 1 for paper, 2 for Scissors\n'))
comp_val = random.randint(0,2)
print(f'computer chooses{comp_val}')

if user_input >=3 or user_input<0:
    print('invalid input')
elif user_input==0:
    if comp_val == 1:
        print('lost')
    elif comp_val == 0:
        print('equal')
    else:
        print('you won')
elif user_input==1:
    if comp_val == 2:
        print('lost')
    elif comp_val == 1:
        print('equal')
    else:
        print('you won')
elif user_input==2:
    if comp_val == 0:
        print('lost')
    elif comp_val == 2:
        print('equal')
    else:
        print('you won')
