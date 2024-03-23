import machine_data

menu = machine_data.menu
resource = machine_data.resources
def reporter():
   for resources_list in resource:
       print(resources_list,resource[resources_list])

user_choose = input('What would you like ?(espresso/latte/cappuccino)')

if user_choose == 'report':
    reporter()

