import random



def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)



def calc_score(cards):
    if sum(cards)>21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

user_card = []
computer_card =[]


for i in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())

user_score = calc_score(user_card)
computer_score = calc_score(computer_card)
print(f'your score = {user_score}')
print(f'computer score {computer_score}')

if user_score == 0 or computer_score == 0 or user_card>21:
    isgame_over = True