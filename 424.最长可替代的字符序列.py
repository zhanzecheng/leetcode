# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/26 下午2:33
# @Author  : zhanzecheng
# @File    : 424.最长可替代的字符序列.py
# @Software: PyCharm
"""
# 这一题的思路竟然是用一个滑动窗口来做
# TODO: check 1
# expressive
class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0
        left = 0
        right = 1
        max_len = 1
        window_max = 1
        dic = {s[0]: 1}

        while right < len(s) + 1 and left <= right:

            if right - left - window_max > k:
                dic[s[left]] -= 1
                if dic[s[left]] == 0:
                    dic.pop(s[left])
                left += 1
            else:
                if right == len(s):
                    right += 1
                    if max_len < right - left - 1:
                        max_len = right - left - 1
                    break
                if s[right] in dic:
                    dic[s[right]] += 1
                else:
                    dic[s[right]] = 1
                right += 1
            window_max = max(list(dic.values()))

            if max_len < right - left - 1:
                max_len = right - left - 1
        return max_len

        # def count_max(self, a):