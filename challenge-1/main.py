age = input('what is your age\n')
totalWeeks = 90*52   #by considering max age of human 90 years
yourWeeks = float(age)*52
left  = totalWeeks-yourWeeks

print(f'you have {left} weeks')