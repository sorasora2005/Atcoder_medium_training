#!/usr/bin/env python
# coding: utf-8

# In[ ]:


s=list(input())
new1 = [x for x in s if x != "a"]
new2 = [x for x in new1 if x!= "e"]
new3 = [x for x in new2 if x!= "i"]
new4 = [x for x in new3 if x!= "o"]
new5 = [x for x in new4 if x!= "u"]
ans="".join(new5)
print(ans)


# In[ ]:


#別解
s=input()
print("".join(i for i in s if i not in "aeiou"))


# In[ ]:


m=int(input())
ds=list(map(int,input().split()))
c=0
mid=(sum(ds)+1)//2
key=0
for i in range(m):
  c+=ds[i]
  if c==mid:
    exit(print(i+1,ds[i]))
  elif c>mid:
    key=i+1
    day=mid-sum(ds[:i])
    exit(print(i+1,day))


# In[ ]:


n=int(input())
p=[]
for _ in range(n):
  a=list(map(int,input().split()))
  p.append(a)
l=sorted(p, key=lambda x: x[1], reverse=True)
key=0
for i,s in enumerate(l):
  if s[0] != l[0][0]:
    key=i
    break
if l[0][0]==l[1][0]:
  exit(print(max(l[0][1]+l[1][1]//2,l[0][1]+l[key][1])))
else:
  exit(print(l[0][1]+l[1][1]))

