# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/2 上午10:45
# @Author  : zhanzecheng
# @File    : 3.字符串里面的最长不重复字符.py
# @Software: PyCharm
"""
# 这一题的核心思路是使用一个hash 保存最近一次字符的位置，然后根据
# dp[i] = min(dp[i-1] + 1, i - loc[s[i]]) 来完成O(n)内的求解

# TODO: check 1

class Solution:
    def lengthOfLongestSubstring(self, s):

        dp = [0] * len(s)
        voc = {s[0] : 0}
        for i in range(1, len(s)):
            if s[i] not in voc:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = min(dp[i-1] + 1, i - voc[s[i]])
            voc[s[i]] = i
        return max(dp)

#
# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         dp = [1] * len(s)
#         result = -1
#         loc = {s[0]:0}
#         for i in range(1, len(s)):
#             if s[i] not in loc:
#                 dp[i] = dp[i- 1] + 1
#             else:
#                 dp[i] = min(dp[i-1] + 1, i - loc[s[i]])
#             result = max(result, dp[i])
#             loc[s[i]] = i
#         return result
if __name__ == '__main__':
    solution = Solution()
    data = 'tmmzuxt'
    print(solution.lengthOfLongestSubstring(data))