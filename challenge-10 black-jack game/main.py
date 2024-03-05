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

def compare(user_score,comp_score):
    if user_score == comp_score:
        return 'Draw'
    elif comp_score ==0:
        return  'Lose'
    elif user_score == 0:
        return 'win with a black jack'
    elif user_score > 21:
        return 'you went over you lose'
    elif user_score > comp_score:
        return 'you win'
    else:
        return 'you lose'



def play_game():

    user_card = []
    computer_card =[]


    for i in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    isgame_over =False

    while not isgame_over:

        user_score = calc_score(user_card)
        computer_score = calc_score(computer_card)
        print(f'your card = {user_card} and your score = {user_score}')
        print(f'computer first card = {computer_card[0]} computer score {computer_score}')

        if user_score == 0 or computer_score == 0 or user_score>21:
            isgame_over = True
        else:
            user_deal = input("Type 'Y' to get another card,Type 'n' to pass")
            if user_deal == 'y':
                user_card.append(deal_card())
            else:
                isgame_over = True

    while computer_score!=0 and computer_score <17:
        computer_card.append(deal_card())
        computer_score = calc_score(computer_card)
    print(f'your final hand ={user_card} and score = {user_score}')
    print(f'computer final hand = {computer_card} and score ={computer_score}')
    print(compare(user_score,computer_score))


    while input('do you want to play game black jack y or n') == 'y':
        play_game()
play_game()