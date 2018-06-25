# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/24 下午3:10
# @Author  : zhanzecheng
# @File    : 331.判断是否是前序序列.py
# @Software: PyCharm
"""


class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        # 这一题是使用栈的好方法
        stack = []
        if preorder == '#':
            return True
        preorder = preorder.split(',')
        for i in preorder:
            if i == '#':
                if len(stack) == 0:
                    return False

                if stack[-1] == '#':
                    while len(stack) > 0 and stack[-1] == '#':
                        if len(stack) < 2:
                            return False
                        stack.pop()
                        stack.pop()

                    stack.append('#')
                else:
                    stack.append('#')
            else:
                stack.append(i)
        return stack == ['#']