class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        time_buy = 0
        profit = 0
        for time in range(1, len(prices)):
            # select best price to buy
            if prices[time_buy] > prices[time]:
                time_buy = time
            profit = max(profit, prices[time] - prices[time_buy])
        return profit
        
def main():
    solution = Solution()
    nums1 = [3, 2, 1, 9, 20, 11, 100,  10, 6] # sorted

    profit = solution.maxProfit(nums1)
    print('profit:',profit)
if __name__ == "__main__":
    main()