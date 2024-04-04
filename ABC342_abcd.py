#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
ABC342
目標50分以内にA-C完答
Dも解き切る
パフォ1000に乗せる

'''


# In[ ]:


s=input()

#s[0]が異なる
if s[0]!=s[1] and s[1]==s[2]:
    exit(print(1))
    
#s[1]～s[-2]が異なる
for i in range(1,len(s)-1):
    if s[i-1]!=s[i] and s[i]!=s[i+1]:
        print(i+1)

if s[-1]!=s[-2] and s[-2]==s[-3]:
    print(len(s))


# In[ ]:


n=int(input())
ps=list(map(int,input().split()))
q=int(input())
for _ in range(q):
    a,b=map(int,input().split())
    A=ps.index(a)
    B=ps.index(b)
    if A<B:
        print(a)
    else:
        print(b)


# In[ ]:


n=int(input())
s=list(input())
q=int(input())
for _ in range(q):
    c,d=input().split()
    for i in range(len(s)):
        if s[i]==c:
            s[i]=d
ans=''.join(s)
print(ans)
'''
TlEなった。たぶん値を保持して全探索
じゃないようにしなきゃいけない。
'''
n=int(input())
s=list(input())
q=int(input())

#atcoderの場合



# In[ ]:


'''
気持ちを切り替えてDを先にやる。
あたりまえだけど、10^5
いやこれも全探索してTLE
いやでも全探索しないで
どうやって調べんねんこれ
全探索しないと無理やろ。

'''

import math
c=0
n=int(input())
aa=list(map(int,input().split()))

for i in range(len(aa)):
    for j in range(i+1,len(aa)):
        ss=aa[i]*aa[j]
        s=math.sqrt(ss)
        if int(s)==s:
            c+=1
print(c)

