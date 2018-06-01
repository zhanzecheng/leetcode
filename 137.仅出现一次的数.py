# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/1 下午4:07
# @Author  : zhanzecheng
# @File    : 137.仅出现一次的数.py
# @Software: PyCharm
"""
import math

# 变态，竟然还有负数的情况
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        add = int(math.pow(2, 30))
        count = {}
        for i in nums:
            i += add
            tmp = self.int2bit(i)
            for c, i in enumerate(tmp[::-1]):
                if c not in count:
                    count[c] = int(i)
                else:
                    count[c] = (count[c] + int(i)) % 3
        tmp = ""
        for i in range(32):
            tmp = str(count[i]) + tmp
        return self.bit2int(tmp) - add


    def int2bit(self, num):
        s = ""
        while num:
            s = str(num % 2) + s
            num = num // 2
        for i in range(32 - len(s)):
            s = '0' + s
        return s
    def bit2int(self, s):
        num = 0
        tmp = 1
        for i in s[::-1]:
            num += int(i) * tmp
            tmp *= 2
        return num
if __name__ == '__main__':
    solution = Solution()
    data = [2,2,3,2, ]
    print(solution.singleNumber(data))