#從1加到100 只加奇數
x=0
for i in range(1,100,2):
    x+=i
print('1+3+5+...+99=',x)

#從1加到100 只加偶數
y=0
for i in range(2,101,2):
    y+=i
print('2+4+6+...+100=',y)

#從1加到100
total=0
for i in range(1,101):
    total+=i
print('1+2+3+...+100=',total)
