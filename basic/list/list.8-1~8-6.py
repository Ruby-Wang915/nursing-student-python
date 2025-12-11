#8-6 計算串列某一元素的個數: count
NL=[4,2,6,6,1,5,1,3,1]
C=NL.count(1)
print(f'出現次數:{C}次')

print()

#8-6 排序:大至小 or 小至大: sort/reverse
NL=[4,2,6,5,1,3]
NL.sort()  #小至大
print(f'NL由小至大:{NL}')

NL.reverse() #大至小 reverse:不排序只顛倒
print(f'NL由大至小:{NL}')

NL=[4,2,6,5,1,3]    
NL.sort(reverse=True)  #合併:sort(reverse=True) 排序又翻轉
print(f'NL由大至小:{NL}')

print()

#8-4~8-5 functions
LS=['A','B','C','D','E','F','G']

#.append(x)
LS.append('X')
print(LS)

#.insert(idx,x)
LS.insert(4,'E')
print(LS)

#.pop(idx)
LS.pop(-1)
print(LS)

#.remove(x) : 移除第一個出現的i
LS.remove('G')
print(LS)


print()


#8-3 slice 切一部分list
#[star:end:jump]
LS=['A','B','C','D','E','F','G']

print(LS[1:3])
print(LS[:3]) #==[0:3]
print(LS[1:])
print(LS[0:-1])

print()

print(LS[0:4:2])
print(LS[::2])
print(LS[::-1]) #反轉 #jump是負的會反轉
print(LS[::-2])

print()

#8-3 一個一個印出串列
LS=['Aa','Bb','Cc','Dd']
for i in range(len(LS)):
    print(LS[i])

print()

#8-2 計算串列長度: len
LS=['Aa','Bb','Cc','Dd']
C=len(LS)
print(C)

print()

#~打錯了怎麼辦
LS=['A','B','D','C']

#LS[2]='C'
#LS[3]='D'

LS[2],LS[3]=LS[3],LS[2] #x,y=y,x
print(LS)

print()

#8-1 建立串列
Student=[8,5,3,'Ruby']
S=Student[3]
print(S)
