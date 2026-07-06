class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isword = False
    

class Node:
    def __init__(self, word):
        self.root = TrieNode()

        for w in word:
            curr = self.root
            for c in w:
                curr = curr.children[c]
            curr.isword = True


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        h = { len(s): 0}
        trie = Node(dictionary).root

        def dfs(i):
            if i in h:
                return h[i]
            
            res = 1 + dfs(i + 1)
            curr = trie
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                
                curr = curr.children[s[j]]
                if curr.isword:
                    res = min(res, dfs(j + 1))
            
            h[i] = res
            return res
        
        return dfs(0)
                


