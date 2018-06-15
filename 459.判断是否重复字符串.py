# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/14 下午2:14
# @Author  : zhanzecheng
# @File    : 459.判断是否重复字符串.py
# @Software: PyCharm
"""
# 这个时间复杂度是o(n^2)


# trick
'''

def repeatedSubstringPattern(self, str):

        """
        :type str: str
        :rtype: bool
        """
        if not str:
            return False
            
        ss = (str + str)[1:-1]
        return ss.find(str) != -1
        
'''
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        for i in range(1, len(s)):
            if self.check_ok(s[:i], s):
                return True
        return False

    def check_ok(self, a, b):
        a_len = len(a)
        b_len = len(b)
        if b_len % a_len != 0:
            return False
        count = b_len // a_len
        i = 0
        while count != 0:
            if a != b[i*a_len:(i + 1) * a_len]:
                return False
            i += 1
            count -= 1
        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.check_ok('ab', 'abab'))