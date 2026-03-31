# https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len (nums) == 1:
            return 1

        nums_set = set (nums)
        seq_len = 0
        max_seq_len = 0

        for n in nums_set:
            if n-1 not in nums_set:
                seq_len = 1                 
                while n + seq_len in nums_set:                                                     
                    seq_len += 1
                max_seq_len = max (max_seq_len, seq_len)
        return max_seq_len
        
