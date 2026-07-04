s=float(input('input your score : '))
L='x'
if s > 90:
    L="A"
elif s > 80:
    L="B"
elif s > 70:
    L="C"
elif s > 60:
    L="D"
else:
    L="E"
print(f'your level is {L}')
