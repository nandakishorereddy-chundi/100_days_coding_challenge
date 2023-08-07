class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        output = []
        for word in words:
            new_words = word.split(separator)
            new_words = [w for w in new_words if len(w) > 0]
            output += new_words
        return output