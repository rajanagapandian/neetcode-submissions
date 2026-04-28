class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        s = set(nums)
        max_length = 1

        for num in nums:
            if num - 1 not in s:
                length = 1
                
                while num + 1 in s:
                    num += 1
                    length += 1
                
                max_length = max(length, max_length)

        return max_length 