#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''目標AC30分
   結果AC21分
   ふーう気持ち良すぎる
s=a,a,b,b,c,a
'''

n=int(input())
s=list(input())
res=[]
for j in range(1,n):
    c=0
    s1=list(set(s[:j]))
    s2=list(set(s[j:]))
    for i in s1:
        if i in s2:
            c+=1
    res.append(c)
    
print(max(res))


# In[ ]:


'''簡潔な書き方
'''

n = int(input())
s = input()
ans = 0
for i in range(1,len(s)):
  x = set(s[:i])
  y = set(s[i:])
  cnt = len(x&y)
  ans = max(ans,cnt)
print(ans)

