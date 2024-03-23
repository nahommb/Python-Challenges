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

def resource_checker(userchoose):
    for i in range(len(resource)):
        if userchoose!='espresso':
            if resource[i] >= menu[userchoose]['ingredient'][i]:
                print('yess')
                return True
        else:
            if i==2:
                return True
            

resource_checker()
def coffe_maker():
    print('please insert coins\n')
    quarters = float(input('How many quarters\n'))
    dimes = float(input('How many dimes\n'))
    nickles = float(input('How many nickles\n'))
    pennies = float(input('How many pennies\n'))

    converted_amount = calculator(quarters=quarters,dimes=dimes,nickles=nickles,pennies=pennies)
    print(f'${converted_amount}')
    if converted_amount >= menu[user_choose]['cost']:
        resource_checker()
        print(user_choose)
        water_left = resource['water'] - menu[user_choose]['ingredients']['water']
        coffee_left = resource['coffee'] - menu[user_choose]['ingredients']['coffee']
        if(user_choose!='espresso'):
            milk_left = resource['milk'] - menu[user_choose]['ingredients']['milk']
            resource['milk'] = milk_left
        resource['water'] = water_left
        resource['coffee'] = coffee_left
        # print(resource['water'])

if user_choose == 'report':
    reporter()

coffe_maker()
reporter()