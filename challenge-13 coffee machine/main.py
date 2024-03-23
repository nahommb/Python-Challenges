import machine_data

menu = machine_data.menu
resource = machine_data.resources
def reporter():
   for resources_list in resource:
       print(f'{resources_list}:{resource[resources_list]}')

user_choose = input('What would you like ?(espresso/latte/cappuccino)')

def calculator(quarters,dimes,nickles,pennies):
    sum = pennies*0.01 + dimes*0.1 + nickles*0.05 + quarters*0.25
    return sum
def coffe_maker():
    print('please insert coins\n')
    quarters = float(input('How many quarters\n'))
    dimes = float(input('How many dimes\n'))
    nickles = float(input('How many nickles\n'))
    pennies = float(input('How many pennies\n'))

    converted_amount = calculator(quarters=quarters,dimes=dimes,nickles=nickles,pennies=pennies)
    print(f'${converted_amount}')
if user_choose == 'report':
    reporter()

coffe_maker()