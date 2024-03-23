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

    isAvialable_resource = False

    if userchoose != 'espresso':

        for available_resource in resource:
            if resource[available_resource] >= menu[userchoose]['ingredients'][available_resource]:
                print('yess')
                isAvialable_resource = True
            else:
                print('nooo')
                isAvialable_resource = False

    else:
        if resource['water']>=menu[userchoose]['ingredients']['water'] and resource['coffee']>=menu[userchoose]['ingredients']['coffee']:
            print('espriesssso yess')
            isAvialable_resource = True
        else:
            print('noo esprso')

    return isAvialable_resource



# resource_checker(user_choose)
def coffe_maker():


        if(resource_checker(user_choose)):
            print('please insert coins\n')
            quarters = float(input('How many quarters\n'))
            dimes = float(input('How many dimes\n'))
            nickles = float(input('How many nickles\n'))
            pennies = float(input('How many pennies\n'))

            converted_amount = calculator(quarters=quarters, dimes=dimes, nickles=nickles, pennies=pennies)
            print(f'Here is ${converted_amount} in charge')
            if converted_amount >= menu[user_choose]['cost']:
                print(user_choose)
                water_left = resource['water'] - menu[user_choose]['ingredients']['water']
                coffee_left = resource['coffee'] - menu[user_choose]['ingredients']['coffee']
                if(user_choose!='espresso'):
                    milk_left = resource['milk'] - menu[user_choose]['ingredients']['milk']
                    resource['milk'] = milk_left
                resource['water'] = water_left
                resource['coffee'] = coffee_left
            else:
                print('you have not enough money')
        else:
            print("not Enough resources")
        # print(resource['water'])

if user_choose == 'report':
    reporter()

coffe_maker()
reporter()