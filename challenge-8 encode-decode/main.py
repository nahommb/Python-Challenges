
alpa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print(len(alpa))

def encode(message , shift_num):
    encoded_message = ''

    for l in message:
        for i in range(0,26):
            if l == alpa[i]:
                # l = alpa[i]
                if i+shift_num >=26:
                    print(alpa[shift_num+i-26])
                else:
                    print(alpa[i+shift_num])



encode('a',25)

