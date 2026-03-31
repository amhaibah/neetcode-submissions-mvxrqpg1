class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s = {}
        dict_t = {}
        for c in s:
            if c in dict_s:
                dict_s[c] = dict_s[c] + 1
            else:
                dict_s[c] = 1
        for c in t:
            if c in dict_t:
                dict_t[c] = dict_t[c] + 1
            else:
                dict_t[c] = 1

        if dict_s == dict_t:
            return True
        return False
            