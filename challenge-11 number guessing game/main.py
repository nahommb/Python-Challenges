
import random

print('Welcom to number guessing game \n I am thinking number between 1 and 100 ')
def_level = input('choose defficulty type "hard" or "esay" \n ')

random_number = random.randint(1,100)

def gues_chacker(random_num , num):
    print(random_num)
    if random_num == num:
        print('yess')


gues_chacker(random_number,10)

