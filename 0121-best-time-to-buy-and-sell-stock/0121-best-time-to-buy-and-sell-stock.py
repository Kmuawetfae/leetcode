class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # final_value = 0
        # for i in range(len(prices)):
        #     value = prices[i]
        #     if value not in stored_value:
        #         temp_list = set(filter(lambda price: price > value, prices[i:]))
        #         for j in temp_list:
        #             if j - value > final_value:
        #                 final_value = j - value
                
        #         stored_value.append(value)

        profit = 0
        buy = prices[0]

        for sell in prices[1:]:
            if sell > buy:
                profit = max(profit, sell - buy)
            else:
                buy = sell
        
        return profit

        return final_value