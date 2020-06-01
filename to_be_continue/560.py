class Solution:
    """
    两次循环就不考虑了，
    一开始没有考虑到负数，所以报错了
    考虑到负数的时候，需要看解析才能做了

    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1}
        pre = 0
        count = 0
        for num in nums:
            pre += num
            
            if (pre-k) in d:
                # print()
                count += d[pre-k]

            
            if pre not in d:
                d[pre] = 1
            else:
                d[pre] += 1
        return count