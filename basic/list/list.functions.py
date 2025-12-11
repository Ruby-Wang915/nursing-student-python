#秀出list裡的值及元素數量
#加上A附加 I插入 R移除 P彈走 輸入Q離開程式
def pLS(PLS):
    print(' ')
    print(f'目前的LS:{PLS}')  #LS 是這個 list 的名字（在外面),PLS 是同一個 list 在函式裡面的暱稱（在函式裡）
    print('==========================================')
    print('| A=append | I=insert | R=remove | P=pop |' )
    print('| Q=Exit ')


LS=['A','B','C','B']

while True:
    pLS(LS) #這是在「呼叫」函式，把 LS 當成參數傳進去
    OP=input('Please input OPkey:')

    if OP=='A' or OP=='a':
        SA=input('Please input string you want to append:')
        LS.append(SA)

    if OP=='I' or OP=='i':
        idx=eval(input('What index number you want to insert:'))
        SI=input('Please input string you want to insert:')
        LS.insert(idx,SI)

    if OP=='R' or OP=='r':
        SR=input('Please input string you want to remove:')
        if SR in LS:
            LS.remove(SR)
        else:
            print(f'{SR} not in the list.')

    if OP=='P' or OP=='p':
        idxP=eval(input('Please input the index number you want to pop:'))
        if  0 <= idxP < len(LS):
            LS.pop(idxP)
        else:
            print(f'{idxP} is out of index.')


    if OP=='Q' or OP=='q':
        print("bye bye")
        break
