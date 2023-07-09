class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c=0
        if len(s) == len(t):
            for i in s:
              if i in t:
                  if s.count(i)==t.count(i):
                    c=c+1
            if c==len(s):
                return True
            else:
                return False
Solution()
