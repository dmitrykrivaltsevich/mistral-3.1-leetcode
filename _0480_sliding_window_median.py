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
# Make edits below this line only
#

from typing import List
import bisect

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if not nums or k == 0:
            return []

        lower = []
        upper = []
        medians = []

        for i in range(len(nums)):
            # Add the current number to the appropriate half
            if len(lower) == 0 or nums[i] <= -lower[0]:
                bisect.insort(lower, nums[i])
            else:
                bisect.insort(upper, nums[i])

            # Balance the halves
            while len(lower) > len(upper) + 1:
                upper.append(-lower.pop(0))
            while len(upper) > len(lower):
                lower.append(-upper.pop(0))

            # Calculate the median for the current window
            if i >= k - 1:
                medians.append(self.calculate_median(lower, upper))

                # Remove the element that is sliding out of the window
                if nums[i - k + 1] <= lower[0]:
                    index = bisect.bisect_left(lower, nums[i - k + 1])
                    del lower[index]
                else:
                    index = bisect.bisect_left(upper, nums[i - k + 1])
                    del upper[index]

        return medians

    def calculate_median(self, lower: List[int], upper: List[int]) -> float:
        if len(lower) > len(upper):
            return float(lower[0])
        else:
            return (lower[0] - upper[0]) / 2.0
