class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur:
                cur[letter] = {}
            cur = cur[letter]

        cur["*"] = ""

    def search(self, word: str) -> bool:
        cur = self.root
        for letter in word:
            if letter not in cur:
                return False
            cur = cur[letter]

        return "*" in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for letter in prefix:
            if letter not in cur:
                return False
            cur = cur[letter]

        return True


class Trie:
    class Node:
        def __init__(self):
            self.isWord = False
            self.children = [None] * 26

    def __init__(self):
        self.root = Trie.Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            index = ord(c) - ord("a")
            if not curr.children[index]:
                curr.children[index] = Trie.Node()
            curr = curr.children[index]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            index = ord(c) - ord("a")
            if not curr.children[index]:
                return False
            curr = curr.children[index]

        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            index = ord(c) - ord("a")
            if not curr.children[index]:
                return False
            curr = curr.children[index]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
