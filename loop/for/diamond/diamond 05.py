n=eval(input('enter layer:'))
for i in range(n,0,-1):
    for j in range(1,n+1):   #內層應該用 n，而不是寫死 4 或 3,原本寫(1,4)
        print(i,end=' ')
    print()

for i in range(2,n+1):
    for j in range(1,n+1):
        print(i,end=' ')
    print()


'''
3 3 3 
2 2 2
1 1 1
2 2 2
3 3 3
'''
