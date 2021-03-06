# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/13 下午1:37
# @Author  : zhanzecheng
# @File    : 678.有效括号string.py
# @Software: PyCharm
"""

# 来回遍历两次
# 需要左右两边进行夹击

# 用了两个堆栈的方法

# TODO: check 1
class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list1 = []
        list2 = []
        for i in s[::-1]:
            if i == '*':
                list2.append(i)
            elif i == ')':
                list1.append(')')
            else:
                if len(list1) > 0:
                    list1.pop()
                else:
                    if len(list2) > 0:
                        list2.pop()
                    else:
                        return False
        flag1 = len(list1) <= len(list2)

        list1 = []
        list2 = []
        for i in s:
            if i == '*':
                list2.append(i)
            elif i == '(':
                list1.append('(')
            else:
                if len(list1) > 0:
                    list1.pop()
                else:
                    if len(list2) > 0:
                        list2.pop()
                    else:
                        return False
        flag2 = len(list1) <= len(list2)
        return flag2 and flag1


if __name__ == '__main__':
    solution = Solution()
    data = ")))((((**))((*(*((*(*))*))*)*))))))"
    print(solution.checkValidString(data))