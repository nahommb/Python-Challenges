import machine_data

menu = machine_data.menu
resource = machine_data.resources

def coffee_machine():

    user_choose = input('What would you like ?(espresso/latte/cappuccino)')
    def reporter():
       for resources_list in resource:
           print(f'{resources_list}:{resource[resources_list]}')
    def calculator(quarters,dimes,nickles,pennies):
        sum = pennies*0.01 + dimes*0.1 + nickles*0.05 + quarters*0.25
        return sum
    def resource_checker(userchoose):
        isAvialable_resource = False

        if userchoose != 'espresso':

            for available_resource in resource:
                if resource[available_resource] >= menu[userchoose]['ingredients'][available_resource]:
                    # print('yess')
                    isAvialable_resource = True
                else:
                    # print('nooo')
                    isAvialable_resource = False

        else:
            if resource['water']>=menu[userchoose]['ingredients']['water'] and resource['coffee']>=menu[userchoose]['ingredients']['coffee']:
                # print('espriesssso yess')
                isAvialable_resource = True
            else:
                print('noo esprso')

        return isAvialable_resource

    def coffe_maker():
            if(user_choose!='report' and resource_checker(user_choose)):
                print('please insert coins')
                quarters = float(input('How many quarters\n'))
                dimes = float(input('How many dimes\n'))
                nickles = float(input('How many nickles\n'))
                pennies = float(input('How many pennies\n'))

                converted_amount = calculator(quarters=quarters, dimes=dimes, nickles=nickles, pennies=pennies)
                print(f'Here is ${converted_amount} in charge')
                if converted_amount >= menu[user_choose]['cost']:
                    print(f'Here is your {user_choose} enjoy')
                    water_left = resource['water'] - menu[user_choose]['ingredients']['water']
                    coffee_left = resource['coffee'] - menu[user_choose]['ingredients']['coffee']
                    if(user_choose!='espresso'):
                        milk_left = resource['milk'] - menu[user_choose]['ingredients']['milk']
                        resource['milk'] = milk_left
                    resource['water'] = water_left
                    resource['coffee'] = coffee_left
                else:
                    print('you have not enough money')
            elif user_choose =='report':
                reporter()
            else:
                print("not Enough resources")
            # print(resource['water'])

    coffe_maker()

user_need = 'y'
while user_need=='y':
    coffee_machine()
    user_need = input('Do you need another ? "Y" or "N"')
