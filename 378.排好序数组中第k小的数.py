# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/19 下午2:02
# @Author  : zhanzecheng
# @File    : 378.排好序数组中第k小的数.py
# @Software: PyCharm
"""

# 我对这一题很无语。。太奇怪了
# 又看了一次，还是觉得太奇怪了

# 这一题用优先队列是一个很好的解法！！
"""

public class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        PriorityQueue<Tuple> pq = new PriorityQueue<Tuple>();
        for(int j = 0; j <= n-1; j++) pq.offer(new Tuple(0, j, matrix[0][j]));
        for(int i = 0; i < k-1; i++) {
            Tuple t = pq.poll();
            if(t.x == n-1) continue;
            pq.offer(new Tuple(t.x+1, t.y, matrix[t.x+1][t.y]));
        }
        return pq.poll().val;
    }
}

class Tuple implements Comparable<Tuple> {
    int x, y, val;
    public Tuple (int x, int y, int val) {
        this.x = x;
        this.y = y;
        this.val = val;
    }
    
    @Override
    public int compareTo (Tuple that) {
        return this.val - that.val;
    }
}
"""
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        L, R = matrix[0][0], matrix[n - 1][n - 1]

        while L < R:
            mid = (L + R) >> 1
            temp = sum([self.binary_search(y, mid, n) for y in matrix])
            if temp < k:
                L = mid + 1
            else:
                R = mid
        return L

    def binary_search(self, row, x, n):
        L, R = 0, n
        while L < R:
            mid = (L + R) >> 1
            if row[mid] <= x:
                L = mid + 1
            else:
                R = mid
        return L

if __name__ == '__main__':
    solution = Solution()
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
             ]
    k = 8,
    d = [1, 4, 6, 8, 9, 10, 11, 12]
    print(solution.kthSmallest(matrix, 6))