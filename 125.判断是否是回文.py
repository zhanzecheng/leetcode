# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/24 下午7:33
# @Author  : zhanzecheng
# @File    : 125.判断是否是回文.py
# @Software: PyCharm
"""
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        data = ""
        for d in s:
            if str.isalnum(d):
                data += d
        data = data.lower()
        return data == data[::-1]