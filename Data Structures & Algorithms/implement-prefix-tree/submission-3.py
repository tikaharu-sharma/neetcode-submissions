class PrefixTree:

    def __init__(self):
        self.full_word = []
        self.prefixes = []

    def insert(self, word: str) -> None:
        self.full_word.append(word)
        for i in range(len(word)):
            self.prefixes.append(word[:i])

    def search(self, word: str) -> bool:
        if word in self.full_word:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        if prefix in self.prefixes or prefix in self.full_word:
            return True
        return False
        