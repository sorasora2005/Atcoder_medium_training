#!/usr/bin/env python
# coding: utf-8

# In[ ]:


N = int(input())
A = list(map(int, input().split()))
d = [0]*9
for i in A:
  if i >= 3200:
    d[-1] += 1
  else:
    d[i//400] = 1
print(max(1, sum(d[:-1])), sum(d[:-1])+d[-1])


# In[ ]:


'''色なんでもよいを8種類の中で何でもよいじゃなくてほんとに
全部の中から何でもよい。なんだって。それをおれは勘違いしてて
解けんかった。あとは普通に最初の処理のとこの記述が下手すぎた。
たしかに入力i//400の部分を1にしてあげる。っていうの納得だわ。
うますぎる。sumで要素の和をとる。

'''
res=[]
n=int(input())
m=list(map(int,input().split()))
m.sort()
cc=0 #3200以上のレートの人の数を数える

for i in range(n):
    if 1<=m[i]<=399:
        res.append("灰色")
    elif 400<=m[i]<=799:
        res.append("茶色")
    elif 800<=m[i]<=1199:
        res.append("緑色")
    elif 1200<=m[i]<=1599:
        res.append("水色")
    elif 1600<=m[i]<=1999:
        res.append("青色")
    elif 2000<=m[i]<=2399:
        res.append("黄色")
    elif 2400<=m[i]<=2799:
        res.append("橙色")
    elif 2800<=m[i]<=3199:
        res.append("赤色")
    else:#レートが3200以上の場合の処理
        cc+=1
        
R=set(res)
ans=len(R)+cc

#全員がレート3200以上の時の処理
if len(R)==0 and cc>0: 
    exit(print(1,ans))

print(len(R),ans)   

