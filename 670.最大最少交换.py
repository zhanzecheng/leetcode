# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/23 上午9:38
# @Author  : zhanzecheng
# @File    : 670.最大最少交换.py
# @Software: PyCharm
"""

# TODO: check 1

# 在有数字的情况下，应该尽量想到哈希表
class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num:
            return 0
        # 因为数字是从0到9的，我们可以使用哈希的方式来进行存储
        num = list(str(num))

        dic = {}
        for i in range(len(num)):
            dic[int(num[i])] = i
        for i in range(len(num)):
            for j in range(int(num[i])+1, 10)[::-1]:
                if j in dic and i < dic[j]:
                    num[dic[j]] = num[i]
                    num[i] = str(j)
                    value = "".join(num)
                    return eval(value)
        value = "".join(num)
        return eval(value)
if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumSwap(99368))