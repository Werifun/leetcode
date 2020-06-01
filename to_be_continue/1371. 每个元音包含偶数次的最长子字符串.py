class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        ans, status = 0, 0
        pos = [-1]*32
        pos[0] = 0
        for i in range(len(s)):
            if s[i] == 'a':
                status ^= 1<<0
            elif s[i] == 'e':
                status ^= 1<<1
            elif s[i] == 'i':
                status ^= 1<<2
            elif s[i] == 'o':
                status ^= 1<<3
            elif s[i] == 'u':
                status ^= 1<<4
            else:
                pass

            if pos[status] >=0:
                ans = max(ans, i-pos[status]+1)
            else:
                pos[status] = i + 1
            
        return ans
            
