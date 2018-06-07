# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/6 上午11:29
# @Author  : zhanzecheng
# @File    : 208.实现一个trie树.py
# @Software: PyCharm
"""

class Node:
    def __init__(self, char='*'):
        self.char = char
        self.count = 0
        self.is_word = False
        self.child = []

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            find_char = False
            childs = node.child
            for child in childs:
                if child.char == c:
                    find_char = True
                    node = child
                    break
            if not find_char:
                tmp = Node(c)
                node.child.append(tmp)
                node = tmp
        # define it is the last char
        node.is_word = True

    # 你这里循环递归，需要一个标志来指引啊
    def dfs(self, node, word):
        for c in word:
            if c == '.' and len(word) == 1:
                for n in node.child:
                    if n.is_word:
                        return True
                return False
            if c == '.':
                flag = False
                for n in node.child:
                    flag = flag or self.dfs(n, word[1:])
                    if flag:
                        return True
                return flag

            find_char = False
            childs = node.child
            for child in childs:

                if child.char == c:
                    if len(word) == 1:
                        return child.is_word

                    return self.dfs(child, word[1:])
            if not find_char:
                return False

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        node = self.root
        if word == '.':
            for n in node.child:
                if n.is_word:
                    return True
            return False
        if word[0] == '.':
            flag = False
            for n in node.child:
                flag = flag or self.dfs(n, word[1:])
                if flag:
                    return True
            return flag
        return self.dfs(node, word)

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            find_char = False
            childs = node.child
            for child in childs:
                if child.char == c:
                    find_char = True
                    node = child
            if not find_char:
                return False
        return True


        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)
"""
["WordDictionary","","","","","","search","addWord","search","search","search","search","search","search"]
[[],[""],[""],[""],[""],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]
"""
if __name__ == '__main__':
    trie = Trie()
    trie.addWord('at')
    trie.addWord('and')



    print(trie.search('a.d'))