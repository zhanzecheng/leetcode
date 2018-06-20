# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/19 下午1:53
# @Author  : zhanzecheng
# @File    : 367.完美平方.py
# @Software: PyCharm
"""

class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l = 0
        high = num
        if num == 1:
            return True
        while l <= high:
            mid = (l + high) // 2
            print(mid)
            tmp = mid * mid
            if tmp == num:
                return True
            elif tmp < num:
                l = mid + 1
            else:
                high = mid - 1
        return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.isPerfectSquare(16))