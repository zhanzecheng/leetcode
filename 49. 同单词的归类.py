# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/23 下午7:42
# @Author  : zhanzecheng
# @File    : 49. 同单词的归类.py
# @Software: PyCharm
"""


'''
直接用排序就可以做
并且 "".join 可以联合数组中的值
'''
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        for s in strs:
            tmp = "".join(sorted(s))
            if tmp not in result:
                result[tmp] = [tmp]
            else:
                result[tmp].append(s)
        return list(result.values())


if __name__ == '__main__':
    solution = Solution()
    d = ["eat","tea","tan","ate","nat","bat"]
    print(solution.groupAnagrams(d))