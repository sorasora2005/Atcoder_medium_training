#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''<自分の解答>
 【感想】いや。むずかったです。あの、普通にWAだったし。
 　　　　まず最初の入力の時にボタンの数値を全部－1にすれば
     　　インデックスとボタン番号が対応できた。
       　あとは基本的に-1を出力するんだけど、条件満たせば
         exit(関数)で関数を実行してプログラム終わらす。
         あとはwhileで中途半端にやるんじゃなくて同じの続けちゃっても
　　　　 いいからforで一定回数繰り返しやるべきだった。そこらへんかな
     　　まじで解答きれいすぎて泣くわ。'''

n=int(input())
As=[]
for _ in range(n):
    As.append(int(input()))

if As[0]==1:
    print(-1)

next_index=1
c=1
nums=[1]

if (1 in As and 2 in As):
    while As[next_index-1] != 2:
        next_index=As[next_index-1]
        c+=1
        nums.append(next_index)
        if len(nums) != len(set(nums)):
            c=-1
            break

print(c) 


# In[ ]:


'''<他人の回答>'''

n=int(input())
a=[int(input())-1 for i in range(n)]
p=0
for i in range(n):
  p=a[p]
  print(p)
  if p==1:exit(print(i+1))
print(-1)


# In[ ]:


'''<自分の回答修正版>'''

n=int(input())
As=[]
for _ in range(n):
    As.append(int(input()))
p=1
c=0
x=0
while x==0 and c<n:
        p=As[p-1]
        c+=1
        if p==2:
            x=1
if x==0:
    print(-1)
else:
    print(c) 

