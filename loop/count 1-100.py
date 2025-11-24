#從1加到100 只加奇數
odd=0
for i in range(1,100,2):
    odd+=i
print('1+3+5+...+99=',odd)

#從1加到100 只加偶數
even=0
for i in range(2,101,2):
    even+=i
print('2+4+6+...+100=',even)

#從1加到100
total=0
for i in range(1,101):
    total+=i
print('1+2+3+...+100=',total)

