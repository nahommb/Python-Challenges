import random

no_of_letters = int(input("how many letters u want\n"))
no_of_symbols = int(input('how many symbols u want\n'))
no_of_numbers = int(input('how many nubers u want\n'))

letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
    'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['/', '@', '#', '$', '%', '&']

password = ''

for i in range(0, no_of_letters):

    random_let = random.choice(letters)
    password += random_let

for i in range(0, no_of_symbols):
    random_symbol = random.choice(symbol)
    password += random_symbol
for i in range(0, no_of_numbers):
    random_num = random.choice(numbers)
    password += random_num

char_list = list(password)
random.shuffle(char_list)

password = ''.join(char_list)
print(f'your password = {password}')
