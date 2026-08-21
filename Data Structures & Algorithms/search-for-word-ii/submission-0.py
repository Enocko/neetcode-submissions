class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isword = False 
    
    def addWord(self, word):
        curr = self
        for w in word:
            curr = curr.children[w]
        curr.isword = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        visited = set()
        res = set()
        def dfs(r, c, node, word):
            if (r >= len(board) or c >= len(board[0]) or
                r < 0 or c < 0 or (r, c) in visited or board[r][c] not in node.children):
                return 
            
            visited.add((r, c))
            word += board[r][c]
            node = node.children[board[r][c]]

            if node.isword:
                res.add(word)

            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)

            visited.remove((r, c))
    

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, root, '')
        
        return list(res)
                
        

