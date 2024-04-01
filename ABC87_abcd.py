#!/usr/bin/env python
# coding: utf-8

# In[ ]:


x=int(input())
a=int(input())
b=int(input())
print(x-a-(b*((x-a)//b)))


# In[ ]:


a=int(input())
b=int(input())
c=int(input())
x=int(input())
count=0
s=[]

for i in range(0,a+1):
    for j in range(0,b+1):
        for k in range(0,c+1):
            s.append(500*i+100*j+50*k)
            
for t in range(len(s)):
    if s[t]==x:
        count+=1
print(count)


# In[ ]:


'''
全選び方の総数はn=100通り
なので全探索ですべてのAを求める

'''
n=int(input())
As=list(map(int,input().split()))
Bs=list(map(int,input().split()))
ans=[]

for i in range(n):
    ss=0
    for j in range(0,i+1):
        ss+=As[j]
    for k in range(i,n):
        ss+=Bs[k]
    ans.append(ss)
print(max(ans))


# In[ ]:


'''
新種のタイプの問題すぎないか？

'''
n=int(input())
m=int(input())
xs=[0]*10**10
#まず-10<=0<=10ぐらいで考える
g=10**5
pn=[]

#1回目
l,r,d=map(int,input().split())
xs[g]=l
xs[g+d]=r
pn.append(l)
pn.append(r)

#2回目
l,r,d=map(int,input().split())
if l in pn:
 
#やってみる。
n=int(input())
m=int(input())
ls=[]
rs=[]
ds=[]
    
for _ in range(m):
    l,r,d=map(int,input().split())
    ls.append(l)
    rs.append(r)
    ds.append(d)

    
for i in range(m):
    if ls[i]==ls[0]:
        
#だめだどう考えてもわからない。
#何をどうしたらいいか想像つかない

