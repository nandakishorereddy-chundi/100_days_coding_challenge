from collections import Counter
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        s_freq = Counter(s)
        g_freq = Counter(goal)
        if len(s) != len(goal) or len(s) == 1 or len(goal) == 1:
            return False
        if s == goal:
            fg = 0
            for k in s_freq:
                if s_freq[k] > 1:
                    fg = 1
                    break
            if fg:
                return True
            return False
        n = len(s)
        chrs1 = set()
        chrs2 = set()
        cnt = 0
        for i in range(n):
            if s[i] != goal[i]:
                cnt += 1
                chrs1.add(s[i])
                chrs2.add(goal[i])
        if cnt != 2 or len(chrs1.intersection(chrs2)) != 2:
            return False
        return True