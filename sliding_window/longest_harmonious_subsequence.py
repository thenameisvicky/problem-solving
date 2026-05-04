from typing import List


class Solution_LongestHarmoniousSubsequence:
    def LongestHarmoniousSubsequence(self, nums: List[int]) -> int:
        left = 0
        max_harmonius = 0
        nums.sort()
        for right in range(len(nums)):
            while nums[right] - nums[left] > 1:
                left += 1
            if nums[right] - nums[left] == 1:
                max_harmonius = max(max_harmonius, right - left + 1)
        return max_harmonius
