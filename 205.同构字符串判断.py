# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/28 上午9:28
# @Author  : zhanzecheng
# @File    : 205.同构字符串判断.py
# @Software: PyCharm
"""


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m, n = len(s), len(t)
        if m != n:
            return False

        mapDict = {}
        toDict = {}
        for i in range(m):
            if s[i] not in mapDict:
                mapDict[s[i]] = t[i]
            else:
                if t[i] != mapDict[s[i]]:
                    return False

            if t[i] not in toDict:
                toDict[t[i]] = s[i]
            else:
                if s[i] != toDict[t[i]]:
                    return False
        return True
