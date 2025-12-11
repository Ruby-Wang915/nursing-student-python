#題目:自動分類機 輸入一些數字 把奇數偶數分別放進一個列表裡
numbers = input('enter numbers: ').split(' ') #輸入:2 3 4 5

odds = []
evens = []

for num_str in numbers:
    num = int(num_str)
    if num % 2 == 0:      
        evens.append(num) #把這個數字加進偶數串列 #注意是括弧
    else:
        odds.append(num) #把這個數字加進奇數串列

print(f'奇數 {odds}')
print(f'偶數 {evens}')
