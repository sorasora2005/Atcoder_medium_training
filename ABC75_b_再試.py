#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''<俺なりにいろいろ思考してみたけど、絶対この書き方だめだわ
　　ってので解けなかった。> 
   ちょっとこれもう一回解こう。
'''

h,w=map(int,input().split())
ss=[]
ans=[[0]*w]*h

for _ in range(h):
    ss.append(list(input()))
       
for i in range(1,len(ss)-2):
    for j in range(1,len(ss[i]-2)):
        if ss[i][j]=="#":
            ans[i][j]="#"
        else:
            c=0
            if ss[i-1][j-1]=="#":
                c+=1
            if ss[i-1][j]=="#":
                c+=1
            if ss[i-1][j+1]=="#":
                c+=1
            if ss[i][j-1]=="#":
                c+=1
            if ss[i][j+1]=="#":
                c+=1
            if ss[i+1][j-1]=="#":
                c+=1
            if ss[i+1][j]=="#":
                c+=1
            if ss[i+1][j+1]=="#":
                c+=1
            ss[i][j]=c
            
for j in range(1,len(ss[1]-1)
    
print(ss)


# In[ ]:


'''<人の解答>
 【感想】まじですごすぎるわ。forを4回繰り返すのか。最後の書き方のところも
 　　　　勉強になる。'''

h, w = map(int, input().split())
g = [input() for _ in range(h)]
ans = [[-1] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if g[i][j] == "#":
            ans[i][j] = "#"
            continue
        cnt = 0
        for di in range(-1, 2):
            for dj in range(-1, 2):
                ni, nj = i + di, j + dj
                if ni in range(h) and nj in range(w) and g[ni][nj] == "#":
                    cnt += 1
        ans[i][j] = cnt
for i in range(h):
    print(*ans[i], sep="")

