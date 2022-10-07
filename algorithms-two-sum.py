#https://leetcode.com/problems/two-sum/

"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order ."""

num = [2, 7, 3, 1, 2, 5]
target = 6

def twoSum(arr, tar=4):
    for index, value in enumerate(arr):
        for indexAdditive, valueAdditive in enumerate(arr):
            if index != indexAdditive:
                sum = value + valueAdditive
                if sum == tar:
                    print(index, indexAdditive)
twoSum(num, target)
