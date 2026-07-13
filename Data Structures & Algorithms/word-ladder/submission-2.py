class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        visited = set()
        wordList = set(wordList)
        queue = deque()
        queue.append([beginWord, 1])

        while queue:
            word, length = queue.popleft()
            for j in range(len(word)):
                c = "abcdefghijklmnopqrstuvwxyz"
                for char in c:
                    new_word = word[:j] + char + word[j+1:]
                    if new_word == endWord:
                        return length + 1
                    if new_word in wordList and new_word not in visited:
                        queue.append([new_word, length+1])
                        visited.add(new_word)
        return 0
                

