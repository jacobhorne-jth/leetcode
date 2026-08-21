class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            
            curr = curr.children[ch]
        
        #now at end
        curr.is_end = True
        

    def search(self, word: str) -> bool:
        #use a dfs approach is slightly faster
        def dfs(i, node):
            if i == len(word):
                return node.is_end

            ch = word[i]

            if ch == ".":
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True
                return False

            if ch not in node.children:
                return False

            return dfs(i + 1, node.children[ch])

        
        return dfs(0, self.root)
    '''
    def search(self, word: str) -> bool:
        possible = [self.root]

        for ch in word:
            next_possible = []

            for node in possible:
                if ch == ".":
                    next_possible.extend(node.children.values())

                else:
                    if ch in node.children:
                        next_possible.append(node.children[ch])

            possible = next_possible


            if not possible:
                return False

        return any(node.is_end for node in possible)
    '''

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)



#two approaches
"""
First create TrieNode class = has children dict and is_end bool
#adding word is simple, use self.root and walk through the trie
#do that by checking if each ch in word is in the curr pointers children dict
#add it if not
#remember to add curr.is_end = True at the end

biggest thing was search
searching could be same except for the dot feature
most optimal solution is to track possible ones
when reaching ., have to add all possible ones

#can do that with a list of possible and a next_possible, updating possbile with next_possible
which is either appending for each non . char or extended with . char's children

however, because this adds every possible one, its slower than dfs which would stop after first valid one

track index
#dfs(i = 0, node = self.curr)

within dfs, base case = len(word) == i: return node.is_end (cause only if a word ends there)

iterate through node.children.values and for each child:
check if child = . call dfs and return True if dfs(i + 1, child)
otherwise return false
check if ch itself is in node.children (none = return False)
then call dfs(i + 1, node.childrenp[ch])



#Time and Space:
#for add: O(n) for both, going through all of word, or stor ing n trienodes
for search: dots vs no dots:
no dots: O(n) for time, 
space: O(1) for non dfs solution, O(n) for dfs cause recursive stack

dots:
worst case, dfs:
O(26^n), O(n)
because could be 26 options if n dots

worst case, bfs/iterative
O(26^n), O(26^n)
dfs has better space cause recrusive stack + only one path at a time
this one migth look at all of them
"""