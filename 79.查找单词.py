# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/5 上午9:28
# @Author  : zhanzecheng
# @File    : 79.查找单词.py
# @Software: PyCharm
"""
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self .flag = False
        row = len(board)
        col = len(board[0])
        trace = [[0] * len(board[0]) for _ in range(len(board))]



        def dfs(i, j, word, c):

            if i < row and i >= 0 and j >= 0 and j < col and trace[i][j] != -1 and c < len(word):
                trace[i][j] = -1
                if word[c] == board[i][j]:
                    if c == len(word) - 1:
                        self.flag = True
                    dfs(i+1,j,word,c+1)
                    if self.flag == False:
                        dfs(i - 1, j, word, c + 1)
                    if self.flag == False:
                        dfs(i, j+1, word, c + 1)
                    if self.flag == False:
                        dfs(i, j-1, word, c + 1)
                    trace[i][j] = 0

                else:
                    trace[i][j] = 0

                    return
            return
        for i in range(row):
            for j in range(col):
                dfs(i, j, word, 0)
                if self.flag:
                    return True
        return False
if __name__ == '__main__':
    solution = Solution()
    data =[
          ['A','B'],
          ['S','F'],
        ]
    print(solution.exist(data,'ABFS'))

