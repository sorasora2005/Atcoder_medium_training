#!/usr/bin/env python
# coding: utf-8

# In[ ]:


my_list = ['a', 'b', 'c', 'd']
index_to_remove = 2  # 'c' を削除したい場合

# pop() を使う方法
my_list.pop(index_to_remove)

# スライスを使って削除する別の方法
my_list = my_list[:index_to_remove] + my_list[index_to_remove+1:]

#reversed()を使って逆順で実行
for item in reversed(my_list):
    print(item)

# range(start, stop, step) を使って逆順のインデックスを生成する。
for i in range(len(my_list) - 1, -1, -1):
    print(my_list[i])


# In[ ]:


'''<自分の解答>
 【感想】簡単だね。殴るよ？ '''

a=list(input())
for i in range(len(a)-1,-1,-1):
    a.pop(i)
    b=a[:len(a)//2]
    c=a[len(a)//2:]
    if b==c:
        print(2*len(b))
        break

