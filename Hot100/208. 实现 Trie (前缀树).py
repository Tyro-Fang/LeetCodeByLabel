#1.set方式
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.TrieSet = set()
        


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.TrieSet.add(word)


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word in self.TrieSet:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        pLen = len(prefix)
        for i, word in enumerate(self.TrieSet):
            if word[:pLen] == prefix:
                return True
        return False




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


#2.前缀树
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.isEnd = False
        self.children = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        ptr = self
        for i, w in enumerate(word):
            if w not in ptr.children:
                ptr.children[w] = Trie()
            ptr = ptr.children[w]
        ptr.isEnd = True



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        ptr = self
        for _, w in enumerate(word):
            if w not in ptr.children:
                return False
            ptr = ptr.children[w]
        return ptr.isEnd



    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        ptr = self
        for _, w in enumerate(prefix):
            if w not in ptr.children:
                return False
            ptr = ptr.children[w]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)