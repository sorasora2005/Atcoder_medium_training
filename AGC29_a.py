#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''<自分の解答>
 【感想】はぁ。もうしんどすぎるわ。必死にやったのにTLE
 　　　　なったし。勘弁してくれよ。マジでわからん。
     　　素直に解いたらこうなるし。ふざけんなよボケ。
       　はぁ。結構きついな。なんで？もうきついって。はぁ。'''

s=list(input())
c=0
f=1
while f==1:
    for i in range(len(s)-1):
        if (s[i]=='B' and s[i+1]=='W'):
            s[i]='W'
            s[i+1]='B'
            c+=1
    if s==sorted(s,reverse=True):
        f=0
print(c)


# In[ ]:


'''<他人の解答１>
 【感想】このアルゴリズムは思いつかんて。w同士で場所が入れ替わる
 　　　　ことないからっていうのを利用している。なるほど。たしかにforを
     　　whileの中で繰り返すのは怪しいと思わなきゃいけないな。'''

S = list(input())
N = len(S)

white = []
black = []

for i, s in enumerate(S):
    if s == "W":
        white.append(i)
    else:
        black.append(i)

count = 0
for i, w in enumerate(white):
    count += w-i
print(count)


# In[ ]:


'''<他人の解答２>
 【感想】うーん。きれいすぎてうなるww '''

S=input()
N=len(S)
count=0
stack=0
for i in range(N):
  if S[i]=="W":
    count+=i-stack
    stack+=1
print(count)

