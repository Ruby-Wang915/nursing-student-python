def check_systolic(bp):
    if bp<90:
        return 'LOW'
    elif bp<=119:
        return 'NORMAL'
    else:
        return 'HIGH'
    
bp=int(input('Enter systolic blood pressure:'))
result=check_systolic(bp)
print('Blood pressure category:',result)

