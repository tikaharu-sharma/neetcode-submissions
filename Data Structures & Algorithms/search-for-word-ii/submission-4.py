class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1
        self.endofWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ##create a words Trie first

        root = TrieNode()

        for i in range(len(words)):
            curr = root
            word = words[i]

            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.index = i
            curr.endofWord = True
        
        row, col = len(board), len(board[0])
        res = []
        visited = set()
        def dfs(r, c, curr):
            if r<0 or c<0 or r==row or c==col or (r,c) in visited:
                return 
            
            if board[r][c] not in curr.children:
                return
            
            next_node = curr.children[board[r][c]]

            if next_node.endofWord:
                res.append(words[next_node.index])
                next_node.endofWord = False

            visited.add((r,c))
            dfs(r-1, c, next_node)
            dfs(r+1, c, next_node)
            dfs(r, c+1, next_node)
            dfs(r, c-1, next_node)
            visited.remove((r,c))
            return 
        
        for r in range(row):
            for c in range(col):
                dfs(r, c, root)
        return res













