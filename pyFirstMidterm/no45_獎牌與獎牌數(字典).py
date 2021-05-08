medals={}
n=int(input("輸入筆數n："))
while (n<=4):
    for i in range(1,n+1):
        name,num=input("").split(" ")
        medals[name]=num
    item1=medals.items()
    for m1,m2 in item1:
        print("%s牌得到%s面" % (m1,m2))

