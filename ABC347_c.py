#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#目標20分AC
n,a,b=map(int,input().split())
ds=list(map(int,input().split()))
'''
次の数が休日の中に入っているか、
来週または再来週の休日に入って
いればよい。'''

a=[n*(a+b) for n in range(3)]
print(a)

a=3
b=[i+j*7 for i in range(1,a+1) for j in range(0,3) ]
print(b)

'''
結局全然できなかった。無理だろこれむずい

'''


# In[ ]:


n,a,b=map(int,input().split())
d=list(map(int,input().split()))
b=[i+j*(a+b) for j in range(0,1000) for i in range(0,a)]
for i in d:
    if i-j not in b:
        break
    exit(print("Yes"))
print("No")
#てことはどうすればいいんだ。アルゴリズムが違う根本的に


# In[ ]:


n,a,b=map(int,input().split())
d=list(map(int,input().split()))
for i in d:
        c=(i)%(a+b)
        if 0=<c=<a-1:
            pass
        else:
            break
        exit(print("Yes"))
print("No")


# In[ ]:


n,a,b=map(int,input().split())
d=list(map(int,input().split()))

for j in range(a):
    for i in d:
        c=(i)%(a+b)
        if 0=<c=<a-1:
            pass
        else:
            break
        exit(print("Yes"))
print("No")

