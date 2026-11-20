class Solution:
    def arrangeCoins(self, n: int) -> int:
                
        return int((-1 + ((1 + (n * 8)) ** 0.5)) / 2)