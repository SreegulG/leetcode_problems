class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [-1]*len(prices)
        return self.solve(prices,dp,0)
        
    
    def solve(self,prices,dp, i = 0):
        if i == len(prices):
            return 0
        if dp[i] != -1:
            return dp[i]
        non_pick = self.solve(prices,dp,i+1)
        pick = 0
        if i>0 and prices[i-1] < prices[i]:
            pick = prices[i]-prices[i-1] + self.solve(prices,dp,i+1)

        dp[i] =  max(pick,non_pick)
        return dp[i]
