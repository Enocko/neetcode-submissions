class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            curr = curr.children[w]
        
        curr.word = True

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for v in curr.children.values():
                        if dfs(i+1, v):
                            return True
                    return False
                else:
                    if c in curr.children:
                        curr = curr.children[c]
                    else:
                        return False
            return curr.word

        return dfs(0, self.root)