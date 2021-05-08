f,g,h,i,j=list(input("輸入五張牌：").split(" "))
cards={"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}
total=(cards[f])+(cards[g])+(cards[h])+(cards[i])+(cards[j])
print("加總值："+str(total))