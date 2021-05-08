n=int(input("輸入一個度數："))

if(n<=120):
    print("Summer months:", n*2.1)
    print("Non-Summer months:",n*2.1)

elif(121<=n<=330):
    print("Summer months:",(120*2.1)+(n-120)*3.02)
    print("Non-Summer months:",(120*2.1)+(n-120)*2.68)

elif(331<=n<=500):
    print("Summer months:",(120*2.1)+(210*3.02)+(n-120-210)*4.39)
    print("Non-Summer months:",(120*2.1)+(210*3.02)+(n-120-210)*3.61)

elif(501<=n<=700):
    print("Summer months:",(120*2.1)+(210*3.02)+(170*4.39)+(n-120-210-170)*4.97)
    print("Non-Summer months:",(120*2.1)+(210*3.02)+(170*4.39)+(n-120-210-170)*4.01)

elif(n>701):
    print("Summer months:",(120*2.1)+(210*3.02)+(170*4.39)+(200*4.97)+(n-120-210-170-200)*5.63)
    print("Non-Summer months:",(120*2.1)+(210*3.02)+(170*4.39)+(200*4.97)+(n-120-210-170-200)*4.50)

