class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c in ['(', '[', '{']:
                st.append(c)
            else:
                if c == ')':
                    if not st or st[-1] != '(':
                        return False
                if c == ']':
                    if not st or st[-1] != '[':
                        return False
                if c == '}':
                    if not st or st[-1] != '{':
                        return False
                st.pop()
        if len(st) != 0:
            return False
        return True