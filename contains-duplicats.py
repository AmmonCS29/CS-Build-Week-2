'''
Understand:
    -Input going to be an array of numbers
    -find if the array has duplicate numbers
    - return True if a value appears more than once in the array
    - return False if it is unique
    Objective: Return True or False depending on if the array contains at leaset one duplicate pair. 
    
Planning: 
    -create dict
    -iterate over list
    -if it is not in the dict. assign it to dictionary with value of one
        -return false
    -else
        - return true
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for number in nums:
            if number in d:
                return True
            else: 
                d[number] = 1
        return False
