class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}
        for c in s:
            count_s[c] = count_s.get(c, 0) + 1
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        
        for k in count_s.keys():
            if not k in count_t or count_s[k] != count_t[k]:
                return False
        
        for k in count_t.keys():
            if not k in count_s or count_s[k] != count_t[k]:
                return False
            
        return True

        