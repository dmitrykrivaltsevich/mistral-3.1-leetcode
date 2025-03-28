# Problem:
# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.
#
# For examples, if arr = [2,3,4], the median is 3.
# For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
# You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
#
# Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.
#
#
#
# Example 1:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
# Explanation:
# Window position                Median
# ---------------                -----
# [1  3  -1] -3  5  3  6  7        1
#  1 [3  -1  -3] 5  3  6  7       -1
#  1  3 [-1  -3  5] 3  6  7       -1
#  1  3  -1 [-3  5  3] 6  7        3
#  1  3  -1  -3 [5  3  6] 7        5
#  1  3  -1  -3  5 [3  6  7]       6
# Example 2:
#
# Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
# Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
#
#
# Constraints:
#
# 1 <= k <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
#
# Make sure the implementation can handle nums size of 100000 and k=50000. The "heapq" solution is not performant enough for this case.
# Do not use "heapq" -- it is not working for this problem. The "bisect" seems to be working, but doesn't pass all tests, be careful.
# Try to solve using single sorted list as a window.
# Make edits below this line only
#
from sortedcontainers import SortedList
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
        Calculate the median for each sliding window of size k in the given array.

        Args:
            nums (List[int]): The input list of integers.
            k (int): The size of the sliding window.

        Returns:
            List[float]: A list containing the medians of each sliding window.
        """

        if not nums or k == 0:
            return []

        medians = []
        window = SortedList(nums[:k])

        # Calculate the median of the first window
        if k % 2 == 1:
            medians.append(window[k // 2])
        else:
            medians.append((window[k // 2 - 1] + window[k // 2]) / 2)

        # Slide the window across the array
        for i in range(k, len(nums)):
            window.add(nums[i])
            window.remove(nums[i - k])

            if k % 2 == 1:
                medians.append(window[k // 2])
            else:
                medians.append((window[k // 2 - 1] + window[k // 2]) / 2)

        return medians
