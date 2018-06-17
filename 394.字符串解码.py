# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/16 下午7:20
# @Author  : zhanzecheng
# @File    : 394.字符串解码.py
# @Software: PyCharm
"""
# 用stack来解决的问题

class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp = ""
        i = 0
        while True:
            while i < len(s):
                # print('asd')
                if s[i] >= '1' and s[i] <= '9':
                    count = 0
                    for pp in range(i, len(s)):
                        if s[pp] >= '0' and s[pp] <= '9':
                            count = count * 10 + int(s[pp])
                        else:
                            pp -= 1
                            break
                    print(count)
                    i = pp
                    p = 1
                    for j in range(i+2, len(s)):
                        if s[j] == ']':
                            p -= 1
                        elif s[j] == '[':
                            p += 1
                        if p == 0:
                            break
                    tmp = tmp + count * s[i+2:j]
                    # print(s[i+2:j], count)
                    i = j
                else:
                    tmp += s[i]
                i += 1
            if ('[' in tmp) == False:
                break
            s = tmp
            i = 0
            tmp = ""
        return tmp
if __name__ == '__main__':
    solution = Solution()
    data = '10[a]'
    print(solution.decodeString(data))
