# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/2 上午10:45
# @Author  : zhanzecheng
# @File    : 3.字符串里面的最长不重复字符.py
# @Software: PyCharm
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [1] * len(s)
        result = -1
        loc = {s[0]:0}
        for i in range(1, len(s)):
            if s[i] not in loc:
                dp[i] = dp[i- 1] + 1
            else:
                dp[i] = min(dp[i-1] + 1, i - loc[s[i]])
            result = max(result, dp[i])
            loc[s[i]] = i
        return result
if __name__ == '__main__':
    solution = Solution()
    data = 'tmmzuxt'
    print(solution.lengthOfLongestSubstring(data))