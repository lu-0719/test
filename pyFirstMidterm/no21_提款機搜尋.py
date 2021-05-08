n=int(input("請輸入查詢組數："))
data=[["123","456","9000"],["456","789","5000"],["789","888","6000"],
["336","558","10000"],["775","666","12000"],["566","221","7000"]]
for i in range(0,n):
    ac,pwd=input("輸入帳號及密碼：").split(" ")
    if ac==data[0][0] and pwd==data[0][1]:
        print(data[0][2])
    elif ac==data[1][0] and pwd==data[1][1]:
        print(data[1][2])
    elif ac==data[2][0] and pwd==data[2][1]:
        print(data[2][2])
    elif ac==data[3][0] and pwd==data[3][1]:
        print(data[3][2])
    elif ac==data[4][0] and pwd==data[4][1]:
        print(data[4][2])
    elif ac==data[5][0] and pwd==data[5][1]:
        print(data[5][2])
    else:
        print("error")