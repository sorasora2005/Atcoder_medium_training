#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#模範解答、なんか似た問題やったわ。マジでこれうざいむずい。できなきゃ。

h,w,n=map(int,input().split())
s=[['.']*w for _ in range(h)]
i=j=dj=0
di=-1
for _ in range(n):
    if s[i][j]=='.':
        s[i][j]='#'
        di,dj=dj,-di
    else:
        s[i][j]='.'
        di,dj=-dj,di
    i=(i+di)%h
    j=(j+dj)%w
for i in s:
    print(*i,sep="")


# In[ ]:


s=input()
for i in range(len(s)-1,-1,-1):
    if s[i]==".":
        ss=s[i+1:]
        exit(print(ss))
        

