class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        start, end = 0, len(nums) - 2

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] < nums[mid + 1]:
                start = mid + 1
            else:
                end = mid - 1
        return start