class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for time in range(1, len(prices)):
            if prices[time] > prices[time - 1]:
                profit += prices[time] - prices[time - 1]
        return profit

def main():
    solution = Solution()
    prices = [7,1,5,3,6,4]
    result = solution.maxProfit(prices)
    print('result',result)
    
if __name__ == "__main__":
    main()