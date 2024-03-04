
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

num1 = float(input('Enter First Number\n'))
for symbol in oprerations:
    print(symbol)
user_choice = input('choice operation')
num2 = float(input('Enter Second Number \n'))

calc = oprerations[user_choice]
calc(num1,num2)



next = True

# while next:
#     num1 = float(input('Enter First Number\n'))
#     user_choice = input('choice operation')
#     num2 = float(input('Enter Second Number \n'))
#     result =0
#     if user_choice =='+':
#        result = add(num1, num2)
#     elif user_choice =='-':
#         result = sub(num1,num2)
#     elif user_choice =='*':
#        result = mul(num1,num2)
#     elif user_choice =='/':
#        result = div(num1,num2)
#     else:
#         print('invalid operator')
#     can_cantin = input(f"Type 'y to continue calculating with {result} or 'n' to start new calaculation\n")
#     if can_cantin == 'n':
#         next = False