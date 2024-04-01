#!/usr/bin/env python
# coding: utf-8

# In[ ]:


m=int(input())
x=48-m
print(x)
#3分


# In[ ]:


a,b=map(int,input().split())
s=input()
c=["0","1","2","3","4","5","6","7","8","9"]
for i in range(0,a):
    if s[i] in c:
        pass
    else:
        exit(print("No"))
if s[a]=="-":
    pass
else:
    exit(print("No"))
for j in range(a+1,a+b+1):
    if s[j] in c:
        pass
    else:
        exit(print("No"))
print("Yes")

'''
一個だけWAとれなくて何かと思ったら二個目のfor
をs[j]じゃなくてs[i]でやってた。ふざけんなよ
マジで。注意。直前で気づいてよかった。


# In[ ]:


import re

# 入力
a, b = map(int, input().split())
s = input()

# 正規表現パターンを構築
pattern = f'^\\d{{{a}}}-\\d{{{b}}}$'

# パターンマッチング
if re.match(pattern, s):
    print("Yes")
else:
    print("No")

#gptの解答、正規表現


# In[ ]:


n=int(input())
cs=[]
ss=[]
fs=[]

for _ in range(n-1):
    c,s,f=map(int,input().split())
    cs.append(c)
    ss.append(s)
    fs.append(f)
#最初に駅1にいる電車についての処理
x=0
mt=ss[0]
time=mt+cs[0]

for i in range(1,n-1):
    x=-(-(time-ss[i])//fs[i])
    mt=ss[i]+x*fs[i]-time
    time=time+mt+cs[i]

#最初に駅2にいる電車の処理
x=0
mt=ss[1]
time=mt+cs[1]


#これを表現
times=[]
for j in range(n-1):
    x=0
    mt=ss[j]
    time=mt+cs[j]
    for i in range(j+1,n-1):
        x=-(-(time-ss[i])//fs[i])
        mt=ss[i]+x*fs[i]-time
        time=time+mt+cs[i]
    times.append(time)
times.append(0)

for i in times:
    print(i)
    
#草案


# In[ ]:


n=int(input())
cs=[]
ss=[]
fs=[]

for _ in range(n-1):
    c,s,f=map(int,input().split())
    cs.append(c)
    ss.append(s)
    fs.append(f)

#これを表現
times=[]
for j in range(n-1):
    x=0
    mt=ss[j]
    time=mt+cs[j]
    for i in range(j+1,n-1):
        x=-(-(time-ss[i])//fs[i])
        mt=ss[i]+x*fs[i]-time
        
        if time<ss[i]:
            mt=ss[i]-time
            
        time=time+mt+cs[i]
    times.append(time)
times.append(0)

for i in times:
    print(i)
  
'''
提出したけどsample 2/3 test 5/10
だった。でもちゃんと方針立ててえらいと思うんだけど
何がダメだったんだろう。
'''
'''
なるほど、駅に着いたときに電車がまだ発車時刻じゃなかったら
mtはtime-ss[i]になるのか。うわーくそ惜しいわ。
つめがあまいよ。気づこうね。

'''


# In[ ]:


N = int(input())
CSF = [list(map(int, input().split())) for _ in range(N - 1)]

for start in range(N):
  now = 0
  for i in range(start, N-1):
    c, s, f = CSF[i]
    if now <= s:
      now = s
    else:
      now = (now + f - 1) // f * f
    now += c
  print(now)
'''
まぁやってることは同じだね。
ちゃんと状況を把握するのみ。
その力を付けていこう
'''

