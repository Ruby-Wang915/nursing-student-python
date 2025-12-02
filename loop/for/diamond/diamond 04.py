n=eval(input("enter layer:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()

for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()


#i用來控制「第幾次」、「第幾列」、「第幾層」

'''
print(東西, end=" ")
在「同一行」上，一個一個「排隊印東西」，中間用空白隔開，不換行。

print()
這一行印完了，「換行」，開始下一行。

* 
* * 
* * * 
* * * * 
* * * 
* * 
* 
'''
