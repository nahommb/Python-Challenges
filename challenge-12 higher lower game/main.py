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

    first_person = gameGenerator()['A']


    while right:
        second_person = gameGenerator()['B']
        # nextPerson =
        print(f"A : {first_person['name']}\n VS")
        print(f"B : {second_person['name']}")
        usre_chooese = input('who has more followers\n')
        if first_person['followers'] >= second_person['followers'] and usre_chooese=='a':
            score+=1
            print(f'you get your score = {score}')

        elif second_person['followers'] >= first_person['followers'] and usre_chooese=='b':
            score += 1
            print(f'you get your score = {score}')
            first_person = second_person
        else:
            print(f'you lost your score = {score}')
            right =False
        list_of_celeb.append(first_person)

game()