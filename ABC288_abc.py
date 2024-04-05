#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    print(a+b)


# In[ ]:


n,k=map(int,input().split())
ss=[]
for _ in range(k):
    s=input()
    ss.append(s)
s.sort()
for i in s:
    print(i)
            


# In[ ]:


'''
c問題はunion-find木というアルゴリズムで
高速に実行できる。これは頻出の問題なので
あらかじめACLというAtcoder公式のライブラリ
によって提供されている。すごいね。

'''

from atcoder.dsu import DSU
n,m=map(int,input().split())
uf=DSU(n)
ans=0
for _ in range(m):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    if uf.leader(a)!=uf.leader(b):
        uf.merge(a,b)
    else:
        ans+=1
print(ans)

