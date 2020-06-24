'''
Understand: 
    -array of numbers
    -return two indecies of the two numbers that add up to the target number
    -only one solution 
    -each element is used only once
    objective: Take the array of numbers and find the two that add up to the target number
    
Planning: 
    -create a dictionary
    -iterate over the array
    -subtract the target from each element
    -index and value at that
    -append to a new array
    -loop through new array and old array comparing the two numbers.
    
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [d[target - nums[i]], i]
            else: 
                d[nums[i]] = i
