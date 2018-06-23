# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/22 下午1:40
# @Author  : zhanzecheng
# @File    : 567.涵盖字符串的排列.py
# @Software: PyCharm
"""

# 这里使用滑动窗口可以解决，但有个问题就是list的比较不会超时吗
# 当然不会，因为这是英文字母，只有26个选择

class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        # 这一题可以采用滑动窗口的方式来做
        dic1 = {}
        dic2 = {}
        for i in range(len(s1)):
            if s1[i] in dic1:
                dic1[s1[i]] += 1
            else:
                dic1[s1[i]] = 1

            if s2[i] in dic2:
                dic2[s2[i]] += 1
            else:
                dic2[s2[i]] = 1

        j = 0
        for i in range(len(s1), len(s2)):
            if dic1 == dic2:
                return True
            if s2[i] in dic2:
                dic2[s2[i]] += 1
            else:
                dic2[s2[i]] = 1
            dic2[s2[j]] -= 1
            if dic2[s2[j]] == 0:
                dic2.pop(s2[j])
            j += 1
            # print(dic1, dic2)

        return dic1 == dic2