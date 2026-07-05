#format格式化輸出
#print(format(item,format-specifier))
#靠左：<　靠右：>　置中：^

#整數 : d
print(format(100,'8d'))
print(format(100,'08d'))
print(format(100,'>8d'))
print(format(123456,'^8d'))

#浮點數 : f
print(format(20.5,'8.1f'))
print(format(20.5,'08.1f'))
print(format(20.5,'>8.1f'))

#字串 : s
print(format('Ruby has an apple','>20s'))
print(format('Ruby has an apple','>020s'))

