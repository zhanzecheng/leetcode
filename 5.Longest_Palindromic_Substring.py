# -*- coding: utf-8 -*-
"""
# @Time    : 2018/3/17 下午2:10
# @Author  : zhanzecheng
# @File    : 5.Longest_Palindromic_Substring.py
# @Software: PyCharm
"""
'''
对于回文子串，每增加一个字符，最多是加一或者加二
这里需要注意的是 对于切片时最后一个不取
'''
# 他这里其实是有个值来保存开始的位置和最大长度

# 动态规划的题

# 核心公式 还是 +1 + 2

# TODO: check 1
class Solution:
    def longestPalindrome(self, s):
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return s
        maxLen = 0
        start = 0
        length = len(s)
        for i in range(length):
            if i >= maxLen + 1 and s[i - (maxLen + 1): i + 1] == s[i - (maxLen + 1): i + 1][::-1]:
                start = i - (maxLen + 1)
                maxLen += 2
            elif i >= maxLen and s[i - (maxLen): i + 1] == s[i - (maxLen): i + 1][::-1]:
                start = i - (maxLen + 0)
                maxLen += 1

            if i == 0:
                start = 0
                maxLen = 1
        return s[start: start + maxLen]