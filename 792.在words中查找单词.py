# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/15 上午11:41
# @Author  : zhanzecheng
# @File    : 792.在words中查找单词.py
# @Software: PyCharm
"""

# 利用了 hash 和 折半查找的方法


values = [1, 2, 3, 5, 6]
cur = 6

low = 0
high = len(values) - 1
while low < high:
    mid = (low + high) // 2
    if values[mid] >= cur:
        find_flag = True
        high = mid - 1
    elif values[mid] < cur:
        low = mid+1
print(low)

cur = values[low]
print(cur)