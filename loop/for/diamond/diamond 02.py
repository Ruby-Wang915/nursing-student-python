n=eval(input('enter layar:'))

for i in range(1,n+1):
    for j in range(1,i+1):   
        print(j,end=" ") 
    print("")

for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

'''
1
1 2
1 2 3
1 2 3 4
1 2 3
1 2
1
'''
