# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/26 上午9:49
# @Author  : zhanzecheng
# @File    : 842.分割成F序列.py
# @Software: PyCharm
"""
# 这是一题单纯的考察dfs的题

class Solution:
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        self.result = []
        def dfs(string, tmp):

            if not string or len(string) < 0 :
                if len(tmp) > 2:
                    self.result.append(tmp)
                    return tmp

            for i in range(len(string)):
                if int(string[:i+1]) > 2147483647:
                    continue
                if len(self.result) > 0:
                    return
                if len(tmp) >= 2:
                    if int(tmp[-1]) + int(tmp[-2]) == int(string[:i + 1]):
                        if string[0] == '0' and i > 0:
                            continue
                        dfs(string[i + 1:], tmp + [int(string[:i + 1])])
                else:
                    if string[0] == '0' and i > 0:
                        continue
                    dfs(string[i + 1:], tmp + [int(string[:i + 1])])
        dfs(S, [])
        return self.result[0] if len(self.result) > 0 else []

if __name__ == '__main__':
    solution = Solution()
    data = '0123'
    print(solution.splitIntoFibonacci(data))