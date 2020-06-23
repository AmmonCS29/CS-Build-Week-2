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
        # create a dictionary to store the values
        d = {}
        
        #iterate over the provided list of numbers
        for number in nums:
            
            #if the number is in the dictionary return true
            if number in d:
                return True
            
            #else add the number to the dictionary with the value of 1
            else: 
                d[number] = 1
                
        #if the value is not in the dictionary at all then retun false. 
        return False
