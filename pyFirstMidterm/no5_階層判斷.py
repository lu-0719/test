M=int(input("請輸入階層值M："))
i=n=1
while (M>=i):   ##True往下執行
    i=i*n
    n+=1
print("超過M為"+str(M)+"的最小階層N值為:"+str(n-1))
