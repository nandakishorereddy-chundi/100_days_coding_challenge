class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        f_s = Counter(s)
        f_t = Counter(t)
        for k in f_s:
            if k not in f_t:
                return False
            if f_s[k] != f_t[k]:
                return False
        for k in f_t:
            if k not in f_s:
                return False
            if f_t[k] != f_s[k]:
                return False
        return True