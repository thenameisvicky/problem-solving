from typing import List

class Solution_defuse_the_bomb:
    def defuse_the_bomb(self, code: List[int], k: int) -> List[int]:
        result=[]
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