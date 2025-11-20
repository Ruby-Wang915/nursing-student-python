






saving=10000
while(saving>=100):
    M=eval(input("輸入提取金額(最低提出100元):"))
    if M<100:
        print("最低100")
    elif M>saving:
        print("你的存款不足")
    else:
        print(f"已提取{M},存款剩餘{saving-M}")
        saving-=M







import random as rd  #載入 random 模組，改名 rd
N=eval(input("enter number:"))
NoH=0 #是 head 的次數累計
i=1
while i<N:
    R=rd.randint(0,1) #tail 0/head 1
    NoH+=R #每次把 R 加到 NoH，等於遇到 1 就加 1,0不影響
    i+=1
print(f"Head:{NoH}")
print(f"percentage={NoH/N:5.1%}") #百分比格式、小數點後 1 位、欄寬 5 顯示




n1=eval(input("P n1:"))
op=input("P op:")
n2=eval(input("P n2:"))

if(op=="**" or op=="+" or op=="-" or op=="*" or op=="/"):
    rv=eval(f"{n1}{op}{n2}")
    print(rv)
else:
    print("invalid op")