from sliding_window.contains_duplicate_II import Solution_containsNearbyDuplicate
from sliding_window.longest_harmonious_subsequence import (
    Solution_LongestHarmoniousSubsequence,
)
from sliding_window.defuse_the_bomb import Solution_defuse_the_bomb

contains_duplicate_solution = Solution_containsNearbyDuplicate.containsNearbyDuplicate(
    Solution_containsNearbyDuplicate, nums=[1, 2, 3, 1], k=3
)

longest_harmonius_subsequence_solution = (
    Solution_LongestHarmoniousSubsequence.LongestHarmoniousSubsequence(
        Solution_LongestHarmoniousSubsequence, nums=[1, 3, 2, 2, 5, 2, 3, 7]
    )
)

defuse_the_bomb_solution = Solution_defuse_the_bomb.defuse_the_bomb(
    Solution_defuse_the_bomb, code=[2,4,9,3], k=-2
)

print(contains_duplicate_solution)
print(longest_harmonius_subsequence_solution)
print(defuse_the_bomb_solution)
