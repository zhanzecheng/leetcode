# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/13 下午6:59
# @Author  : zhanzecheng
# @File    : 680.有效回文串II.py
# @Software: PyCharm
"""


class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True

        l = 0
        h = len(s) - 1
        while l < h:
            if s[l] == s[h]:
                l += 1
                h -= 1
            else:
                break
        if s[l + 1:h + 1] == s[l + 1:h + 1][::-1]:
            return True
        if s[l:h] == s[l:h][::-1]:
            return True

        return False