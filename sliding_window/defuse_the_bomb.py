from typing import List


class Solution_defuse_the_bomb:
    def defuse_the_bomb(self, code: List[int], k: int) -> List[int]:
        result = []
        for i in range(len(code)):
            start = 0
            if k > 0:
                start = i + 1
            else:
                start = i - abs(k)
            total = 0
            for left in range(abs(k)):
                right = (start + left) % len(code)
                total += code[right]
            result.append(total)
        return result

    def defuse_the_bomb_alt(self, code: List[int], k: int) -> List[int]:
        result = []
        doubled_code = code * 2
        if k < 0:
            start = len(code) - abs(k)
        else:
            start = 1
        window_sum = sum(doubled_code[start : start + abs(k)])
        result.append(window_sum)
        for i in range(1, len(code)):
            window_sum = (
                window_sum
                - doubled_code[start + i - 1]
                + doubled_code[start + i + abs(k) - 1]
            )
            result.append(window_sum)
        return result
