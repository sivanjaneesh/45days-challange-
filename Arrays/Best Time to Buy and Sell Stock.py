class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        min_val=prices[0]

        for i in range(1,len(prices)):
            if prices[i]<min_val:
                min_val=prices[i]

            else:
                diff=prices[i]-min_val
                ans=max(diff,ans)

        return ans

            
