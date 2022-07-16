"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Notes:
Similar to the maximum subarry problem - kadanes algorithm

1. you cannot sell on zeroth day (zeroth index), so initialize purchase_price for the day 0 value.
2. initalize max_profit_so_far to keep track of the max profit 
3. Loop through day 1 (index 1) to till last day.
4. check what will be the profit if we sell that day. purchase can be found in purchase_price.
5. See if the profit is bigger than max_profit_so_far. If it is assign it as the new max profit. if not, leave it.
6. Check if today price is lesser than purchase_price. if yes, update purchase_price with todays purchase price.
7. note, even if we don't find a better selling price with lot of profit, the purchase price is not asked in answer. so it does not need to be accurate in the end.
8. max_profit_so_far won't be affected due to point 7.
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit_so_far = 0
        purchase_price = prices[0]
        days  = len(prices)
        for today in range(1, days):
            net_profit_selling_today = prices[today] - purchase_price
            if net_profit_selling_today > max_profit_so_far:
                max_profit_so_far = net_profit_selling_today
            elif prices[today] < purchase_price:
                    purchase_price = prices[today]
        return max_profit_so_far