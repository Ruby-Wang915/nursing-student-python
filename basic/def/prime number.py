#輸入一個 N，然後從 2 到 N 把所有「被判定為質數的數」印出來
def lsP(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

N=int(input('Please input N:'))
for j in range(2,N+1):
    if lsP(j):
        print(f'{j}',end=' ')
    


#判斷是否質數 divisor<=number**0.5
#def:很常用 解決核心問題
