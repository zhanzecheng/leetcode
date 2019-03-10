# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/19 上午9:36
# @Author  : zhanzecheng
# @File    : 538. 加大查找二叉树.py
# @Software: PyCharm
"""

# 这一题的思路是中序访问，并且左右子树颠倒访问
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 更牛的解法， 颠倒左右序访问
'''
class Solution {
private:
    int cur_sum = 0;
public:
    void travel(TreeNode* root){
        if (!root) return;
        if (root->right) travel(root->right);
        
        root->val = (cur_sum += root->val);
        if (root->left) travel(root->left);
    }
    TreeNode* convertBST(TreeNode* root) {
        travel(root);
        return root;
    }
};
'''

class Solution:
    def convertBST(self, root, values=0):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root

        p = self.get_values(root.right)
        root.val = root.val + p + values
        root.left = self.convertBST(root.left, root.val)
        root.right = self.convertBST(root.right, values)
        return root

    def get_values(self, root):
        values = 0
        if not root:
            return values

        values += root.val
        values += self.get_values(root.left)
        values += self.get_values(root.right)
        return values