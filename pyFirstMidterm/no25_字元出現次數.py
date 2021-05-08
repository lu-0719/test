while True:
    w=input("檢測的字串(end結束)：")
    if w=="end":
        print("檢測結束")
        break
    else:
        s=input("檢測的單一字元：")
        t=w.count(s)
        print("字元%s出現次數為：%d" % (s,t))