print('Welcom to BMI calculator\n')
height = float(input('enter your height\n'))
weight = float(input('enter your weight\n'))
bmi = round(weight/height**2,2)
if bmi<=18.5:
    print(f'under weight bmi = {bmi}')
elif bmi<25:
    print(f'normal weight  bmi = {bmi}')
elif bmi < 30:
    print(f'over weight  bmi = {bmi}')
elif bmi > 35:
    print(f"obsese  bmi = {bmi}")
else:
    print(f'clincal obese  bmi = {bmi}')

