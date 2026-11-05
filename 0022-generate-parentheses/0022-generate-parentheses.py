class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        dp = ["()"]

        for _ in range(1, n):
            curr = set()

            for prev in dp:
                for i in range(len(prev) + 1):
                    curr.add(prev[:i] + "()" + prev[i:])

            dp = list(curr)

        return dp