x=float(input('height:'))
y=float(input('weight:'))
xm=x/100
BMI=y/(xm**2)
print(f'your BMI is {BMI:.1f}')

if BMI < 18.5:
    print('體重過輕')
elif BMI < 24:
    print('體重正常')
elif BMI < 27:
    print('體重過重')
else:
    print('重度肥胖')
