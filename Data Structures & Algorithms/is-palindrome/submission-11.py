class Solution:
    def isPalindrome(self, s: str) -> bool:
        a, b = 0, len(s)-1
        while a < b:
            while a < b and not s[a].isalnum():
                a += 1
            while a < b and not s[b].isalnum():
                b -= 1
            
            if not (s[a].lower() == s[b].lower()):
                return False
            a += 1
            b -= 1
        return True