class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for n in word:
            curr = curr.children[n]
        
        curr.word = True

    def search(self, word: str) -> bool:
        
        def dfs(i, root):
            curr = root

            for j in range(i, len(word)):
                c = word[j]
                if c == '.':
                    for child in curr.children.values():
                        if dfs(j+1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.word
        
        return dfs(0, self.root)
        