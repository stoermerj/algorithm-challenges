"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

nums1 = [1,2,6,7]
nums2 = [3,4,5,8]

try:
    def sortArr(arr1, arr2):
        completeArr = (arr1+arr2)
        completeArr.sort()
        return completeArr
    
    def oddEven(arr):
        lengthOfArr = len(arr) / 2
        if lengthOfArr%1 != 0:
            medianOddLen = len(arr) / 2
            medianOddLen = int(medianOddLen - 0.5) #adding to save a line
            medianOdd = arr[medianOddLen]
            return medianOdd
        elif lengthOfArr%1 == 0:
            medianEvenLen1 = len(arr)/ 2
            medianEvenLen2 = medianEvenLen1 - 1
            medianEven = (arr[int(medianEvenLen1)] + arr[int(medianEvenLen2)]) / 2
            return medianEven
        
    def medianAnswer():
        sortedArr = sortArr(nums1, nums2)
        median = oddEven(sortedArr)
        print(median)
except:
    print("ERROR")

medianAnswer()

