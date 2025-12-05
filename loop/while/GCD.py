#最大公因數
n1,n2=eval(input('enter n1,n2:'))
gcd=0
k=2
while k<=n1 and k<=n2:
    if n1%k==0 and n2%k==0:
        gcd=k
    k+=1
print(gcd)
