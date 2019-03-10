# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/13 下午3:33
# @Author  : zhanzecheng
# @File    : 373.找到K个最小的数组对.py
# @Software: PyCharm
"""
import heapq

# 这一种解法是使用了堆的数据结构
# 这里的堆的优先作用会使 最小的值在上面

# TODO: check 1
def kSmallestPairs( nums1, nums2, k):
    queue = []
    def push(i, j):
        if i < len(nums1) and j < len(nums2):
            heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
    push(0, 0)
    pairs = []
    while queue and len(pairs) < k:
        s, i, j = heapq.heappop(queue)
        print(s, nums1[i], nums2[j], i, j)
        pairs.append([nums1[i], nums2[j]])
        push(i, j + 1)
        if j == 0:
            push(i + 1, 0)
    return pairs

if __name__ == '__main__':
    data1 = [1,1,11]
    data2 = [2,4,6]
    k = 3
    print(kSmallestPairs(data1, data2, k))