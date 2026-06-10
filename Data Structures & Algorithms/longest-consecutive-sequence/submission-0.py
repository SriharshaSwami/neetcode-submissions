class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #First lets create a lookUp of the nums arr
        numSet = set(nums)
        longest = length = 0
        for n in numSet:
        #Checking if n is start of a sequence    
            if n - 1 not in numSet:
                length = 0
        #Checking if the sequence grows
                while (n + length) in numSet:
                    length += 1
        #Updating longest if longer subsequence found
                    longest = max(longest, length)
        return longest