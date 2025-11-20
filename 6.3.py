import random as rd
Ans=rd.randint(1,100)

while True:
    guess=eval(input())
    if guess<1 or guess>100:
        print("範圍錯誤")
    elif guess>Ans:
        print("太大")
    elif guess<Ans:
        print("太小")
    else:
        print("答對")
        break