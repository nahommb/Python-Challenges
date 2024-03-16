import random

list_of_celeb = [
    {
        'name':'Neymar',
        'nationality':'Brazil',
        'profession':'footballer',
        'followers': 38000000
    },
    {
        'name': 'Ronaldo',
        'nationality': 'Portugal',
        'profession': 'footballer',
        'followers': 58000000
    },
    {
        'name': 'Messi',
        'nationality': 'Argentina',
        'profession': 'footballer',
        'followers': 40000000
    },
    {
        'name': 'Salah',
        'nationality': 'Egypt',
        'profession': 'footballer',
        'followers': 18000000
    },
]


def gameGenerator():
    person1 = random.choice(list_of_celeb)
    list_of_celeb.remove(person1)
    person2 = random.choice(list_of_celeb)
    return {'A':person1,"B":person2}



def game():
    print('Welcom to celebrity followers compartion game')
    score = 0
    right = True

    while right:
        list_comp = gameGenerator()

        print(f"A : {list_comp['A']['name']}\n VS")
        print(f"B : {list_comp['B']['name']}")
        usre_chooese = input('who have more followers\n')
        if list_comp['A']['followers']>list_comp['B']['followers'] and usre_chooese=='a':
            score+=1
            print(f'you get your score = {score}')

        elif list_comp['B']['followers']>list_comp['A']['followers'] and usre_chooese=='b':
            score += 1
            print(f'you get your score = {score}')
        else:
            print(f'you lost your score = {score}')
            right =False
        list_of_celeb.append(list_comp['A'])
game()