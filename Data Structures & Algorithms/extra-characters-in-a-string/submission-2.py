class TrieNode: 
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = False
    
class Trie:
    def __init__(self, word):
        self.root = TrieNode()

        for w in word:
            curr = self.root
            for c in w:
                curr = curr.children[c]
            curr.word = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie(dictionary).root
        dp = {len(s): 0}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            res = 1 + dfs(i + 1)
            curr = trie
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break

                curr = curr.children[s[j]]
                if curr.word:
                    res = min(res, dfs(j+1))
            
            dp[i] = res 
            return res
    
        return dfs(0)