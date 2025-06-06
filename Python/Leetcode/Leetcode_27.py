'''
Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''
from unittest import removeResult
def removeElement(nums, val):
    nums[:] = [x for x in nums if x!=val]
    return len(nums)


nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums,val))

