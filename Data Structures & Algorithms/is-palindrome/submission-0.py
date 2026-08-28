class Solution:
    def isPalindrome(self, s: str) -> bool:
        striped= ''.join(ch.lower() for ch in s if ch.isalnum())
        left = 0
        right = len(striped)-1
        for i in range(len(striped)//2):
            if striped[left]!=striped[right]:
                return False
            left+=1
            right-=1
        return True