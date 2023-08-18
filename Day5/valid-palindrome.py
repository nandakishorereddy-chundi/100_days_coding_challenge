class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join([c for c in s if c.isalnum()])
        n = len(s)
        for i in range(n//2):
            if s[i] != s[n-i-1]:
                return False
        return True