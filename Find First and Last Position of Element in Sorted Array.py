"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].


Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
"""

nums = []
target = 0

def findNum(input, output):
    arr = []
    for index, value in enumerate(input):
        if value == target:
            arr.append(index)
    return arr

def checkNotFound(func):
    result = findNum(nums,target)
    if len(result) == 0:
        print([-1,-1])
    elif len(result) > 0:
        print(result)

checkNotFound(findNum)