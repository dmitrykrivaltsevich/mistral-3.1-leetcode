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
#
# Make edits below this line only
#

from typing import List
import heapq

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if not nums or k == 0:
            return []

        max_heap = []  # Max-heap for the smaller half of numbers
        min_heap = []  # Min-heap for the larger half of numbers
        count_max = {}
        count_min = {}

        def add_num(num):
            if len(max_heap) == 0 or num <= -max_heap[0]:
                heapq.heappush(max_heap, -num)
                count_max[num] = count_max.get(num, 0) + 1
            else:
                heapq.heappush(min_heap, num)
                count_min[num] = count_min.get(num, 0) + 1

            # Balance the heaps
            if len(max_heap) > len(min_heap) + 1:
                val = -heapq.heappop(max_heap)
                heapq.heappush(min_heap, val)
                count_max[val] -= 1
                if count_max[val] == 0:
                    del count_max[val]
                count_min[val] = count_min.get(val, 0) + 1
            elif len(min_heap) > len(max_heap):
                val = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -val)
                count_min[val] -= 1
                if count_min[val] == 0:
                    del count_min[val]
                count_max[-val] = count_max.get(-val, 0) + 1

        def remove_num(num):
            if num <= get_median():
                if num in count_max and count_max[num] > 0:
                    count_max[num] -= 1
                    if count_max[num] == 0:
                        del count_max[num]
                    max_heap.remove(-num)
                    heapq.heapify(max_heap)
            else:
                if num in count_min and count_min[num] > 0:
                    count_min[num] -= 1
                    if count_min[num] == 0:
                        del count_min[num]
                    min_heap.remove(num)
                    heapq.heapify(min_heap)

        def get_median():
            if k % 2 == 1:
                return -max_heap[0]
            else:
                return (-max_heap[0] + min_heap[0]) / 2

        result = []
        for i in range(len(nums)):
            add_num(nums[i])
            if i >= k - 1:
                result.append(get_median())
                # Remove the element that is sliding out of the window
                remove_num(nums[i - (k - 1)])

        return result
