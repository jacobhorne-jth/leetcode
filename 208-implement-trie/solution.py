class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]

        curr.is_end = True
        

    def search(self, word: str) -> bool:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                return False
            
            curr = curr.children[ch]
        
        return curr.is_end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for ch in prefix:
            if ch not in curr.children:
                return False

            curr = curr.children[ch]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


#this uses the concept of a trie
#trie is basically a dict of dicts
#use a TrieNode class
#each node has a dict of children (the following letters)
#and is_end variable which tracks if its the end of a word

#each operation, time: O(word) cause it iterates through each
#space: O(word) worst case for insert cause creating that many nodes
#O(1) for the others because working with existing nodes

#Total space = O(n) where n is total characters of all of them

