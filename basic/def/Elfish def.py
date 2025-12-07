'''
題目:有一族精靈的文字，會將大寫英文單字向後位移 3位。
如英文的 A 就是 D 。英文的 Z 則是 C 。
‧ 先選擇 L: 精靈 to 英文 或 E: 英文 to 精靈。
‧ 取得一段要翻譯的文字。
‧ 輸出該文字的翻譯。
'''

def EtoL(e):     #e就是要處理的那個字元的盒子
    Ecode=ord(e) #ord:把字元轉成數字編碼
    Lcode=Ecode+3 #88 89 90
    if Lcode>90:
        Lcode-=26 #回到65(A)
    return chr(Lcode) #最後呈'字' 因此是chr

def LtoE(l):
    Lcode=ord(l)
    Ecode=Lcode-3
    if Ecode<65:
        Ecode+=26 #回到90(Z)
    return chr(Ecode)

def translate(text,mode):
    result=''
    for ch in text:
        if 'A'<=ch<='Z':  #在 Python 裡，字串是可以比較大小的
            if mode=='E':
                result+=EtoL(ch)
            elif mode=='L':
                result+=LtoE(ch)
        else:
            result+=ch   #不是大寫英文的全部「原樣照抄，不翻譯」
    return result

text=input('enter text(大寫):').upper() #.upper() 是把字串全部變成大寫的函式
mode=input('enter mode(E/L):').upper()

ans=translate(text,mode)
print('翻譯結果:',ans)



#EtoL(e)：英文 → 精靈（+3）
#LtoE(l)：精靈 → 英文（-3）
#Ecode:英文數字編碼
#Lcode:精靈數字編碼
#ord:英轉數 chr:數轉英
#A-65 Z-90
#防錯機制:A~Z 大寫英文字母以外的東西

#流程:先把字母轉成數字,+-3,再轉成英文
