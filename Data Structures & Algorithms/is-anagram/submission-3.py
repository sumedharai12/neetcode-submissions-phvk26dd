class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)>=len(t):
            bigger_string = s
            smaller_string = t
        else:
            smaller_string = s
            bigger_string = t

        for i in bigger_string:
            if i in smaller_string:
                bigger_string = bigger_string.replace(i, "", 1)
                smaller_string = smaller_string.replace(i, "", 1)
            else:
                return False

        return True
            
        
        