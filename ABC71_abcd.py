#!/usr/bin/env python
# coding: utf-8

# In[ ]:


x,a,b=map(int,input().split())
if abs(x-a)>abs(x-b):
    print("B")
else:
    print("A")


# In[ ]:


s=input()
al=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in s:
    if i in al:
        n=al.index(i)
        al[n]=0
for i in range(len(al)):
    if al[i]=0:
        pass
    else:
        exit(print(al[i]))
print("None")


# In[ ]:


#標準入力"abccc"を"abc"(順序制御不可)
s="abccc"
S=set(s)#一度setオブジェクトにする
print(S)
a="".join(set(S))#それをjoinで一つの文字列に
print(a)

'''
これを使うと上でいちいち"a","b"...としていたのが
"abc..."のように素早く記述できる。
'''

S=input()
s="".join(set(S))
L="abcdefghijklmnopqrstuvwxyz"
for i in L:
  if i not in S:
    print(i)
    break
else:
  print("None")
    


# In[ ]:


'''
2つ以上のものだけ取り出す。
そのうち最大の二つを取り出す。
一旦最大値2個でやってみる。
'''
n=int(input())
ass=list(map(int,input().split()))
ass.sort()
d=[]
for i in range(len(ass)-1):
    if ass[i]==ass[i+1]:
        d.append(ass[i])

D=list(set(d))
d.sort()

for i in range(len(d)-2):
    if d[i]==d[i+1]==d[i+2]:
        D.append(d[i])
        
D.sort(reverse=True)
if len(D)>1:
    print(D[0]*D[1])
else:
    print(0)



# In[ ]:


from collections import Counter


a = list(map(int, input().split()))

# 棒の長さとその出現回数をカウント
length_counts = Counter(a)
print(length_counts,type(length_counts))
print(type(length_counts.items()),length_counts.items())


# In[ ]:


from collections import Counter

n = int(input())
a = list(map(int, input().split()))

# 棒の長さとその出現回数をカウント
length_counts = Counter(a)

# 出現回数が2回以上の長さを長い順に並べる
lengths = [length for length, count in length_counts.items() if count >= 2]
lengths.sort(reverse=True)

# 最大の面積を計算
if len(lengths) >= 2:
    # 最初の2つの長さを使う（ただし、最初の長さが4本以上ある場合は、それだけで正方形を作ることも可能）
    area = lengths[0] * lengths[1] if length_counts[lengths[0]] < 4 else lengths[0] ** 2
else:
    area = 0

print(area)

#chatgptによるコード、見やすすぎて尊敬
#実行時間も45msだったし。


# In[ ]:


'''
なんかまためっちゃ難しそう。
やれるだけやってみる。20分考えてわかんなかったら
あきらめて解説見よう。
～75分

①２つ   
oswie   
oswie     

②3つ
iswoo    swwi
iswtt     tt

③４つ
eewtt    swwi
sswii    bbtt
わかんねーわ。

'''
n=int(input())
s1=input()
s2=input()

