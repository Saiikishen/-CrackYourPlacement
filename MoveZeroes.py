
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
       
        non_zero_index = 0

        for i in range(len(nums)):

            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1
        

        for i in range(non_zero_index, len(nums)):
            nums[i] = 0


#Moved the non zero digits to the beginning of the list and then appended zeroes till the end of the list 
