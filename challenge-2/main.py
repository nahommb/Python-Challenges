print('Welcom to BMI calculator\n')
height = float(input('enter your height\n'))
weight = float(input('enter your weight\n'))
bmi = weight/height**2
if bmi<=18.5:
    print('under weight')
elif bmi>18.5:
    if bmi<=25:
        print('normal weight')
    elif bmi > 25:
        if bmi <= 30:
            print('over weight')
        elif bmi > 30:
            if bmi <=35:
                    print("obsese")
else:
    print('clincal obese')

