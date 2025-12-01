n=eval(input("enter layer:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=' ')    #印i印i次
    print()

for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()

#兩層 for =
#外層決定「現在是第幾排（第幾次）」，
#內層決定「這一排裡，要做幾次什麼事」。

'''
1
2 2
3 3 3
4 4 4 4
3 3 3
2 2
1
'''
