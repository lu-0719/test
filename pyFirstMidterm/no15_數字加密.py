passwd=list(input("輸入一組四位數字為："))
a=(int(passwd[0])+7)%10
b=(int(passwd[1])+7)%10
c=(int(passwd[2])+7)%10
d=(int(passwd[3])+7)%10
print("加密後的數字為：",str(c)+str(d)+str(a)+str(b))