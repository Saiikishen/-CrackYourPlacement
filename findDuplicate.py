#287. Find the Duplicate Number
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_count = {}
        
        for num in nums:
            if num in num_count:
                return num
            else:
                num_count[num] = 1
