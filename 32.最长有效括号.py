# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/4 上午10:01
# @Author  : zhanzecheng
# @File    : 32.最长有效括号.py
# @Software: PyCharm
"""

# 充分的利用堆栈的功能来做

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) != 0:
                    if s[stack[-1]] == '(':
                        stack.pop()
                    else:
                        stack.append(i)
                else:
                    stack.append(i)

        if len(stack) == 0:
            return len(s)
        maxLen = 0
        a = len(s)
        for i in stack[::-1]:
            if  a -i  > maxLen:
                maxLen = a - i - 1
            a = i
        maxLen = max(a, maxLen)
        return maxLen


if __name__ == '__main__':
    solution = Solution()
    data ='(()))'
    print(solution.longestValidParentheses(data))