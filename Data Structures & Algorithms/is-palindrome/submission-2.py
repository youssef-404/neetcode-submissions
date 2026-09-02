class Solution:
    def isPalindrome(self, s: str) -> bool:
        clear_s = ''
        for ch in s:
            if ch.isalnum():
                clear_s+=ch.lower()
        

        for i in range(len(clear_s)//2):
            if clear_s[i]!=clear_s[len(clear_s)-1-i]:
                return False
        return True