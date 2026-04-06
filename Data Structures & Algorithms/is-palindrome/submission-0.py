class Solution:
    def isPalindrome(self, s: str) -> bool:
        char1 = "".join([c for c in s if c.isalnum()]).lower()
        char_list = list(char1)
        
        L, R = 0, len(char_list) - 1
        
        while R > L:
            if char_list[L] == char_list[R]:  # Characters match
                R -= 1
                L += 1
            else:  # Characters don't match
                return False
        return True
       


    

