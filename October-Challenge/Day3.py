"""
1512. Number of Good Pairs

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
"""
#Brute Force
# Time-Complexity -> O(nlogn)
# Space-Complexity -> O(n)

def numIdenticalPairs(nums: List[int]) -> int:
    nums.sort()
    last_ind = {}
    n = len(nums)
    for i in range(n-1,-1,-1):
        if nums[i] not in last_ind:
            last_ind[nums[i]] = i 
    ans = 0 
    for i in range(n):
        ans += last_ind[nums[i]] - i 
    return ans 

#Optimised
# Time-Complexity -> O(n)
# Space-Complexity -> O(n)

def numIdenticalPairs(nums: List[int]) -> int:
    repeat = {}
    ans = 0 
    for num in nums:
        if num in repeat:
            ans += repeat[num]
            repeat[num] += 1 
        else:
            repeat[num] = 1 
    return ans 