
alpa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encode(message , shift_num):
    encoded_message = ''
    for l in message:
        index_of_letter = alpa.index(l)
        if index_of_letter+shift_num >=26:
            # print(alpa[shift_num+index_of_letter-26])
            encoded_message+=alpa[shift_num+index_of_letter-26]
        else:
            # print(alpa[index_of_letter+shift_num])
            encoded_message += alpa[shift_num + index_of_letter]

    print(f'encoded message = {encoded_message}')

def decode(message,shift_num):
    decoded_message = ''
    for l in message:
        index_of_letter = alpa.index(l)
        decoded_message += alpa[index_of_letter-shift_num]

    print(f'encoded message = {decoded_message}')
direction = input("type 'encode' for encoding and 'decode' for decoding\n").lower()
message = input("enter message\n").lower()
shift_number = int(input('enter shift number\n'))

if direction == 'encode':
    encode(message=message,shift_num=shift_number)
elif direction == 'decode':
    decode(message,shift_number)
else:
    print('wrong conversion choice please correctly')