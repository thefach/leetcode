class Solution:
    def isPalindrome(self, s: str) -> bool:      
        clean_s = ''.join(c for c in s.lower() if c.isalnum())
        reversed_s = clean_s[::-1]
        if clean_s == reversed_s:
            return True
        else:
            return False
 

