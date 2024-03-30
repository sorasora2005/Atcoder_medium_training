#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#目標25分AC

'''余りがならないなんてどうやって示すんだよ。
あまりのリスト作ってそのひとつが
10*4超えるまでループしよう。
結果、29分AC、答えの出力Yesじゃなくて
YESだからWAになったんだと。マジで殴るよ？

'''

a,b,c=map(int,input().split())
for n in range(1,10**4):
    h=n*a
    if h%b==c:
        exit(print("YES"))
print("NO")

'''いやその冷静に考えたら、for i in range(1,b+1):
でよいじゃん。mod bで考えたらね。あほ？頭使え。

'''

