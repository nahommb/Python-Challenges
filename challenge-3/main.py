print("leap year calculator\n")

year = int(input('enter year\n'))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print('leap')
        else:
            print('not leap')
    else:
        print('leap')
else:
    print('not leap')