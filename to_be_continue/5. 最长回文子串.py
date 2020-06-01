class Solution:
    """
    方法一：
    重点是如何确定 ij的递增关系
    方法二：
    向外递推
    """
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ""
        dp = [[False]*n for _ in range(n)]

        for d in range(n):
            for i in range(n):
                j = i+d
                if j>=n: 
                    break
                if d == 0:
                    dp[i][j] = True
                elif d == 1:
                    dp[i][j] = (s[i]==s[j])
                else:
                    dp[i][j] = (dp[i+1][j-1] and (s[i]==s[j]))
                
                if dp[i][j] == True and d+1>len(ans):
                    ans = s[i:j+1]
        return ans
                