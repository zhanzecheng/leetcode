# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/13 下午12:55
# @Author  : zhanzecheng
# @File    : 395.最长的重复K次的字符串.py
# @Software: PyCharm
"""

# TODO:想了半天，结果竟然是使用递归的方式来处理
class Solution:
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0

        min_count = k+11
        c = -1
        dict_v = {}
        # 找到在一个序列里出现次数最少的字符
        for i in s:
            if i not in dict_v:
                dict_v[i] = 1
            else:
                dict_v[i] += 1
        for key, values in dict_v.items():
            if values < min_count:
                min_count = values
                c = key

        if min_count >= k:
            return len(s)
        return max(self.longestSubstring(t, k) for t in s.split(c))