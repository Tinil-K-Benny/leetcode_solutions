class Solution:
    def isPalindrome(self, s: str) -> bool:

        l,r=0,len(s) - 1

        while l<r:
            while l<r and not s[l].isalnum():
                l += 1
            
            while l<r and not s[r].isalnum():
                r -=1

            c1,c2 = s[l].lower(),s[r].lower()

            if c1 != c2:
                return False
            
            l +=1
            r-=1
        
        return True
