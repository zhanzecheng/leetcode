# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/13 下午4:07
# @Author  : zhanzecheng
# @File    : 686.easy_多少次重复字符串.py
# @Software: PyCharm
"""

# 根据长度来找 相应的重复次数
class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if B in A:
            return 1
        length1 = len(A)
        length2 = len(B)
        count = length2 // length1
        if length2 % length1 != 0:
            count += 1
        re = A
        for i in range(count-1):
            re = re + A
        if B in re:
            return count
        elif B in (re+A):
            return count + 1
        else:
            return -1

        # ABCDABCD CDAB

if __name__ == '__main__':
    solution = Solution()
    data1 = "abcd"
    data2 = "cdabcdab"
    print(solution.repeatedStringMatch(data1, data2))