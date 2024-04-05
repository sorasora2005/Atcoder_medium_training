#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Cの解答１
結局、最初のやつで最後何になるかは決まってるから、
a～zがc,dによってどう変わるかを保持して、最後に
sに対して適用する。きれいすぎて泣く。

'''

from string import ascii_lowercase

# 入力の受付
n = int(input())
s = input()
q = int(input())

# 'abc...xyz'の文字列で変換前、変換後を事前に作成
str_before = ascii_lowercase
str_after = ascii_lowercase

for i in range(q):
    c, d = input().split()
    str_after = str_after.replace(c, d)

table = s.maketrans(str_before,str_after)
print(s.translate(table))


# In[ ]:


'''
Dの解答1
マジでむずすぎないかこれ。
どうやったらできるんだ。
まず数学的発想がえぐいし。
それをできたとしても計算量
最大でO(10^7)になるよな。。。
いやあのさ難しすぎない？
'''
N = int(input())
A = list(map(int,input().split()))

table = [0 for _ in range(2*10**5 + 1)]
ans = 0

for i in A:
    j = 2
    x = i
    while j * j <= x:
        while x % (j * j) == 0:
            x //= j * j
        j += 1
    ans += table[x]
    table[x] += 1

print(ans + table[0] * (N - table[0]))



