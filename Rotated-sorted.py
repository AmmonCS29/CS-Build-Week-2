Understanding:
    -sorted array as input
    -it pivots its sorting at an unkown point
    -target value to search for
    -if target is in array return the index
    -else return -1 if not in index
    -no duplicates in array
    -run-time complexity O(log n)
Planning:
    -Iterate over the list
    -if target eqaul to value at index 
        -return index
    -else return -1
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target == nums[i]:
                return i
        return -1
