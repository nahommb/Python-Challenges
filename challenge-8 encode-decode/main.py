
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
message = input("enter message\n")
shift_number = int(input('enter shift number\n'))

encode(message = message,shift_num=shift_number)

