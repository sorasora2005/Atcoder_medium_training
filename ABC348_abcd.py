#!/usr/bin/env python
# coding: utf-8

# In[5]:


n=int(input())
ans=[]
for i in range(1,n+1):
    if i%3==0:
        ans.append("x")
    else:
        ans.append("o")
anss="".join(ans)
print(anss)


# In[ ]:


n=int(input())
XY=[]
for _ in range(n):
    a=list(map(int,input().split()))
    XY.append(a)
    
for i in range(n):
    d=0
    if i==0:
        xy=XY[1:]
    elif i==n-1:
        xy=XY[:n]
    else:
        xy=XY[:i]+XY[i+1:]
        
    for j in range(n-1):
        s=(XY[i][0]-xy[j][0])**2+(XY[i][1]-xy[j][1])**2
        if s>d:
            d=s
            num=XY.index([xy[j][0],xy[j][1]])
    print(num+1)
    
#ここまで19分こっから！


# In[ ]:


#10分考えて無理ならあきらめよう20～30分

n=int(input())
cs=[]
As=[]
for _ in range(n): #10^5
    a,c=map(int,input().split())
    if c in cs:  #10^5
        num=cs.index(c)
        if As[num]>a:
            As[num]=a
    else:
      cs.append(c)
      As.append(a)
            
print(max(As))


# In[ ]:


n=int(input())
e=[]
for _ in range(n): #10^5
    a=list(map(int,input().split()))
    e.append(a)
for i in range(len(e)):
    b=e[i][0]
    c=e[i][1]
    e[i][0]=c
    e[i][1]=b
e.sort()
for i in range(len(e)):
    b=e[i][0]
    c=e[i][1]
    e[i][0]=c
    e[i][1]=b

ans=[e[0][0]]
b=e[0][1]
for i in range(n):#10^5
    if e[i][1]!=b:
        b=e[i][1]
        ans.append(b[i][0])
print(max(ans))
print(b)
print(ans)
    


# In[ ]:


#残り29分、10分で無理ならしゃーない。
'''
D問題
まぁ当たり前だけど、全探索したらO(4^40000)になる。
それぞれの木の深さを検証して効率化
E問題
なーんか結構簡単そうだけどね。
'''

