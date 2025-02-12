from typing import List


class Trie:
    class Node:
        def __init__(self):
            self.isWord = False
            self.children = [None] * 26

    def __init__(self):
        self.root = Trie.Node()

    def insert(self, s):
        curr = self.root
        for c in s:
            index = ord(c) - ord("a")
            if not curr.children[index]:
                curr.children[index] = Trie.Node()
            curr = curr.children[index]
        curr.isWord = True

    def dfsWithPrefix(self, curr, word, res):
        if len(res) == 3:
            return

        if curr.isWord:
            res.append(word)

        for i in range(26):
            if curr.children[i]:
                self.dfsWithPrefix(curr.children[i], word + chr(i + ord("a")), res)

    def getWordsStartWith(self, prefix):
        curr = self.root
        result = []

        for c in prefix:
            index = ord(c) - ord("a")
            if not curr.children[index]:
                return result
            curr = curr.children[index]

        self.dfsWithPrefix(curr, prefix, result)
        return result


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        trie = Trie()
        res = []

        for w in products:
            trie.insert(w)

        prefix = ""
        for c in searchWord:
            prefix += c
            res.append(trie.getWordsStartWith(prefix))
        return res


products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"

print(Solution().suggestedProducts(products, searchWord))
