class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map={}
        pan={}
        for i in range (0, len(s)):
            if s[i] not in map:
                map[s[i]]= 1
            else:
                map[s[i]]+=1
        for j in range (0, len(t)):
            if t[j] not in pan:
                pan[t[j]]= 1
            else:
                pan[t[j]]+=1
        return map== pan