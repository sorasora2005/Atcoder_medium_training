#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#ABC349
s=input()
from collections import Counter
count=Counter(s)
s_count=sorted(count.items(),key=lambda x: x[1])
print(s_count)
c=Counter(item[1] for item in s_count)
print(c)
p=c.values()
print(p)
pp=list(p)
print(pp)
for i in pp:
    if i==0 or i==2:
        pass
    else:
        exit(print("No"))
print("Yes")


# In[ ]:


s=input()
t=input().lower()
print(t)
if t[2]=="x" and t[0] in s and t[1] in s:
    num=s.index(t[0])
    for i in range(num+1,len(s)):
        if s[i]==t[1]:
            exit(print("Yes"))
if t[2]!="x" and t[0] in s and t[1] in s and t[2] in s:
    down=s.index(t[0])
    up=len(s)-1-s[::-1].index(t[2])
    for i in range(down+1,up):
        if s[i]==t[1]:
            exit(print("Yes"))
exit(print("No"))
    
    

