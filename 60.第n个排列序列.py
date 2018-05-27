# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/27 下午7:08
# @Author  : zhanzecheng
# @File    : 60.第n个排列序列.py
# @Software: PyCharm
"""

class Solution:
    def __init__(self):
        self.k = 0

    def _jiecheng(self, n):
        res = 1
        for i in range(1, n+1):
            res *= i
        return res
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        num = [str(x) for x in range(1, n + 1)]
        length = len(num)
        res = []
        count = 1
        while True:
            flag = False
            nn = self._jiecheng(length - count)
            for i in range(len(num) - count + 1, 0, -1):
                print(i, nn, k)
                if i * nn < k:
                    k -= i * nn
                    res.append(i)
                    flag = True
            if not flag:
                res.append(0)

            count += 1
            if len(res) == n:
                break

        tmp = []
        for i in res:
            tmp.append(str(num[i]))
            del num[i]
        if len(num) > 0:
            tmp.append(str(num[0]))
        return "".join(tmp)

if __name__ == '__main__':
    solution = Solution()
    print(solution.getPermutation(2, 2))