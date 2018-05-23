# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/23 上午10:08
# @Author  : zhanzecheng
# @File    : 28.Implement_strStr.py
# @Software: PyCharm
"""


"""
Input: haystack = "hello", needle = "ll"
Output: 2
"""


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0

        lengthStr = len(haystack)
        lengthNeedle = len(needle)
        for i in range(lengthStr - lengthNeedle + 1):
            if haystack[i] != needle[0]:
                continue
            if haystack[i:i + lengthNeedle] == needle:
                return i
        return -1