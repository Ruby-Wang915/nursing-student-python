n=eval(input('enter N:'))
lenN=len(str(n))
lenMax=len(str(n*n)) #最大空間的情況是=N*N

for i in range(1,n+1):
    for j in range(1,n+1):
        print(f'{i:>{lenN}}*{j:>{lenN}}={i*j:>{lenMax}}')
    print('='*(lenN*2+lenMax+2)) #+2:是乘號和等於的座位
