# -*- coding: utf-8 -*-
import os

my_file = open(os.path.join(os.path.abspath('.'), 'text.txt'),'r')

# 读单词
my_list=[] 

for item in my_file.read().split(" "):
  my_list.append(item)

list_len = len(my_list)

# 定义计频函数
def frequency(word):
  fre = 0
  n = 0
  while n < list_len:
      if word == my_list[n]:
          fre += 1
      n += 1
  return fre

# 建立单词-频数字典
my_dict={}

for item in my_list:
  my_dict[item] = frequency(item)

# 频数排序
fre_list = my_dict.values()
fre_list.sort()

# 按频数读key，写新txt
# 这里最好用 path 来自动序列化绝对路径 @guo-yu
new_file = open(os.path.join(os.path.abspath('.'), 'output.txt'), 'w')

for x in fre_list:
  for item in my_dict.keys():
    if my_dict[item] == x:
      new_file.write(str(my_dict[item])+"\n")

new_file.close()
my_file.close()