#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#25分AC
'''方針
全探索むり。
ソートして隣り合う値の数を数える
'''
n=int(input())
As=list(map(int,input().split()))
As.sort()
ans=[]
c=1
for i in range(len(As)-1):
    if d>1:
        continue
    if As[i]==As[i+1]:
        c+=1
    else:
        ans.append(c)
        d=As[i+1]-As[i]#差を保存
        c=1
   

an=0   
if n>2:
    for i in range(len(ans)-2):
        if 
elif n==2:
    
if n==1:
    an=1
print(an)


# In[ ]:


#まってそもそも全然違くない？
#だからソートしてその数+1と
#その数-1の数の個数をこたえなきゃいけない
'''だめだ50分考えてもわからない
模範解答見た。なるほど。そうやって解くのか。なんかこのパターン前もあった気がするわ
でもどうやったらできるようになるんだろう。
'''


# In[ ]:


#解答
N=int(input())
a=list(map(int,input().split()))
M=max(a)
L=[0 for i in range(M+2)]
for i in a:
  if i==0:
    L[i]+=1
    L[i+1]+=1
  else:
    L[i]+=1
    L[i+1]+=1
    L[i-1]+=1
print(max(L),L)

