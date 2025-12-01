n=eval(input('請輸入層數:'))
for i in range(1,n+1): #1~n
    space=" "*(n-i)
    star="*"*(2*i-1) #1、3、5、7
    print(space+star)


for i in range(n-1,0,-1):  #(n-1)~1
    space=" "*(n-i)
    star="*"*(2*i-1) 
    print(space+star)

#for i in range ...
#i出現兩次(重複指定)
#不是有兩個i,是依序被用兩次
#space、star：一樣是被「重複指定」
##重新算一次，把舊的值蓋掉

#若同一時間記不同東西
#for i in range(3):
    #for j in range(2):
        #print(i, j)
