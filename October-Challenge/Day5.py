"""
229. Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]

Time Complexity : O(n)
Space Complexity :O(1)
"""
def majorityElement(self, nums: List[int]) -> List[int]:
    cnt1 = 0 ; ele1 = float('-inf') 
    cnt2 = 0 ; ele2 = float('-inf')
    n = len(nums)
    for i in range(n):
        if cnt1 == 0 and nums[i] != ele2:
            cnt1 = 1
            ele1 = nums[i]
        elif cnt2 == 0 and nums[i] != ele1:
            cnt2 = 1 
            ele2 = nums[i]
        elif nums[i] == ele1:
            cnt1 += 1 
        elif nums[i] == ele2:
            cnt2 += 1 
        else:
            cnt1 -= 1 
            cnt2 -= 1 

    cnt1 , cnt2 = 0 , 0 
    for j in range(n):
        if nums[j] == ele1:
            cnt1 += 1 
        if nums[j] == ele2:
            cnt2 += 1 
    
    ls = []
    if cnt1 > (n//3):ls.append(ele1)
    if cnt2 > (n//3):ls.append(ele2)

    return ls