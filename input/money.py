#1 shopping discount
m=eval(input('input money:'))


if m>=5000:
    total=m*0.95
    print('total money:',total)    
    
elif m>=15000:
    total=m*0.9
    print('total money:',total)    
    
elif m>=25000:
    total=m*0.85
    print('total money:',total)    

elif m>=35000:
    total=m*0.8
    print('total money:',total)    

else:
    print('total money:',m)
