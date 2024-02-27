import random

word_list = ["neymar",'messi','ronaldo']


random_choose = random.choice(word_list)
#
# for letter in random_choose:
#     if letter == gues:
#         print('yess')
#     else:
#         print('noo')

container = []
complet = False
print(f'{random_choose}\n')

for i in range(len(random_choose)):
    container.append('_')


for i in range(len(random_choose)):
    gues = input("enter a letter \n").lower()
    print(random_choose[i])
    for j in range(len(random_choose)):
        if random_choose[j] == gues:
            container[j]= gues


    print(container)

final_word = ''.join(container)
print(final_word)
if final_word == random_choose:
    print('You won')
else:
    print('You Lost')

