
def add(num1,num2):
    print(num1 + num2)
    return num1 + num2
def sub(num1,num2):
    print(num1 - num2)
    return num1 - num2
def mul(num1,num2):
    print(num1*num2)
    return num1 * num2
def div(num1,num2):
    print(num1 / num2)
    return num1 / num2

oprerations = {
    "+":add,
    "-":sub,
    '*':mul,
    '/':div
}

def calculator():
    num1 = float(input('Enter First Number\n'))
    for symbol in oprerations:
        print(symbol)

    next = True

    while next:
        user_choice = input('choice operation')
        num2 = float(input('Enter Second Number \n'))

        calc = oprerations[user_choice]
        answer = calc(num1,num2)
        # print('invalid operator')
        can_cantin = input(f"Type 'y to continue calculating with {answer} or 'n' to start new calaculation\n")
        if can_cantin == 'n':
            next = False
            calculator()
        else:
            num1 = answer
calculator()