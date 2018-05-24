# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/24 上午9:41
# @Author  : zhanzecheng
# @File    : 67.Add_Binary.py
# @Software: PyCharm
"""


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        m = len(a) - 1
        n = len(b) - 1
        result = ""
        count = 0
        while m >= 0 and n >= 0:
            tmp = (int(a[m]) + int(b[n]) + count) % 2
            count = (int(a[m]) + int(b[n]) + count) // 2
            result = str(tmp) + result
            m -= 1
            n -= 1

        while m >= 0:
            tmp = (int(a[m]) + count) % 2
            count = (int(a[m]) + count) // 2
            result = str(tmp) + result
            m -= 1
        while n >= 0:
            tmp = (int(b[n]) + count) % 2
            count = (int(b[n]) + count) // 2
            result = str(tmp) + result
            n -= 1
        if count == 1:
            result = '1' + result
        return result

if __name__ == '__main__':
    solution = Solution()
    a = "1"
    b = "111"
    print(solution.addBinary(a, b))