#6-1 建立迴圈
# 迴圈: 1.已知要跑幾次(1/0式) 2.不知要跑幾次
# while條件式==True的話就會執行,False的話就會終止
# 1.初始值 2.迴圈何時結束 3.每次迴圈的增量or減量

#只加even(1~100)
eventotal=0
k=2
while k<=100:
    eventotal=eventotal+k
    k+=2
print(f'只加even:{eventotal}')

print()

#100加到1
total=0
k=100
while k>=1:
    total=total+k
    k-=1
print(f'100加到1:{total}')

print()

#1加到100
total=0
k=1
while k<=100:
    total=total+k
    k+=1
print(f'1加到100:{total}')
    
print()

#1式
count=1
while count<=5:
    print('Ruby')
    count+=1

print()

#0式
count=0
while count<5:
    print('Ruby')
    count+=1
