#287. Find the Duplicate Number
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_count = {}
        
        for num in nums:
            if num in num_count:
                return num
            else:
                num_count[num] = 1


# Dictionary (Hashmap) Usage: The dictionary num_count is used to keep track of the occurrences of each number.
# Efficiency: The solution iterates through the list only once, making it O(n) in terms of time complexity. The space complexity is O(n) due to the storage needed for the dictionary.
# Return First Duplicate: The method returns as soon as it finds the first duplicate number, ensuring optimal performance.
