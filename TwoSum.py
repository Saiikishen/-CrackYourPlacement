class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_to_index:
                return [num_index[complement], i]
            

            num_index[nums[i]] = i


#Empty dictionary num_index is initialised
#Complement of the numbers in nums is calculated
#If complement exists in num_index then index of num and complement is returned
#else store it in dict with the index of num[i]
