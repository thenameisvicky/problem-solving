from typing import List


class Solution_containsNearbyDuplicate:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window_set = set()
        left = 0
        for right in range(len(nums)):
            if nums[right] in window_set:
                return True
            window_set.add(nums[right])
            if right - left >= k:
                window_set.remove(nums[left])
                left += 1
        return False
