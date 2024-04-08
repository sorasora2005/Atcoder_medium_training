#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#30分でABC３完
#17時05から授業
n,p,d=map(int,input().split())
ds=list(map(int,input().split()))
a=min(ds)
if a+d>p:
    print(p)
else:
    print(a+d)


# In[ ]:


#これだと、[2,3,1]と[2,3,3,1]とかでも上位互換判定されてしまう。
#だから、いったんsetにしてやる。

n,m=map(int,input().split())
b=[]
for _ in range(n):
    a=list(map(int,input().split()))
    b.append(a)
b.sort(reverse=True)
for i in range(len(b)):
    for j in range(i+1,len(b)):
        bb=b[i][2:]
        cc=b[j][2:]
        if all(item in cc for item in bb) and (len(set(bb))<len(set(cc)) or b[i][0]>b[j][0]):
            exit(print("Yes"))
print("No")

