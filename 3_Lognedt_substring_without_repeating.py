# -*- coding: utf-8 -*-
"""
# @Time    : 2018/3/16 下午1:32
# @Author  : zhanzecheng
# @File    : 3_Lognedt_substring_without_repeating.py
# @Software: PyCharm
"""

'''
假设已经目前是最长的字符，那么现在有两种情况：
1）下一个字符没有见过，则logest+=1
2) 下一个字符见过， 则 最前端m = max(, ) logest = max
'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = dict()
        longest = 0
        m = 0
        for i in range(len(s)):
            if s[i] not in dic:
                longest = max(longest, i - m + 1)
            else:
                m = max(m, dic[s[i]] + 1)
                longest = max(longest, i - m + 1)
            dic[s[i]] = i
        return longest