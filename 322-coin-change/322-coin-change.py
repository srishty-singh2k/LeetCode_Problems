class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = amount + 1
        dp = [0] + [MAX for _ in range(amount)]

        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return [dp[amount], -1][dp[amount] >= MAX]