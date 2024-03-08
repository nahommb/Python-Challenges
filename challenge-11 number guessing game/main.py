
import random

print('Welcom to number guessing game \n I am thinking number between 1 and 100 ')
def_level = input('choose defficulty type "hard" or "esay" \n ')


random_number = random.randint(1,100)

def gues_chacker(random_num , user_geuss):
    if random_num == user_geuss:
       return True

is_next_attempt = True
attempt = 0


if def_level == 'hard':
    attempt = 9
    print('Now you have 10 attempts')
elif def_level == 'easy':
    attempt = 4
    print('Now you have 5 attempts')


while is_next_attempt and attempt > 0:
    guess_num = int(input('Make a gues:'))

    if gues_chacker(random_number,guess_num):
        print(f'you won the number is {guess_num}')
        is_next_attempt =False
    elif guess_num > random_number:
        print('Too high')
        print('Guess again')
        print(f'you have {attempt} left')
        attempt-=1
    elif guess_num < random_number:
        print('Too low')
        print('Guess again')
        print(f'you have {attempt} left')
        attempt -= 1
