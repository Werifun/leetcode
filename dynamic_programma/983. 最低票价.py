'''
在一个火车旅行很受欢迎的国度，你提前一年计划了一些火车旅行。在接下来的一年里，你要旅行的日子将以一个名为 days 的数组给出。每一项是一个从 1 到 365 的整数。

火车票有三种不同的销售方式：

一张为期一天的通行证售价为 costs[0] 美元；
一张为期七天的通行证售价为 costs[1] 美元；
一张为期三十天的通行证售价为 costs[2] 美元。
通行证允许数天无限制的旅行。 例如，如果我们在第 2 天获得一张为期 7 天的通行证，那么我们可以连着旅行 7 天：第 2 天、第 3 天、第 4 天、第 5 天、第 6 天、第 7 天和第 8 天。

返回你想要完成在给定的列表 days 中列出的每一天的旅行所需要的最低消费。

 

示例 1：

输入：days = [1,4,6,7,8,20], costs = [2,7,15]
输出：11
解释： 
例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划：
在第 1 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 1 天生效。
在第 3 天，你花了 costs[1] = $7 买了一张为期 7 天的通行证，它将在第 3, 4, ..., 9 天生效。
在第 20 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 20 天生效。
你总共花了 $11，并完成了你计划的每一天旅行。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-cost-for-tickets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

方法更好
https://leetcode-cn.com/problems/minimum-cost-for-tickets/solution/zui-di-piao-jie-by-leetcode-solution/

'''

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        min_price_list = [min(costs)]*len(days)
        # print(min_price_list)
        for iter_id in range(1, len(days)):
            today_price = min_price_list[iter_id-1] + min_price_list[iter_id]
            week_id, month_id = self.find_index(days, iter_id, 7, 30)
            # print('days',days[iter_id],iter_id,'week_id',week_id,'month_id', month_id)
            cur_week_price = costs[1] if week_id==-1 else costs[1] + min_price_list[week_id]
            cur_month_price = costs[2] if month_id==-1 else costs[2] + min_price_list[month_id]
            # print('price',today_price,cur_week_price,cur_month_price)
            min_price_list[iter_id] = min(today_price,cur_week_price,cur_month_price)
        # print(min_price_list)
        return min_price_list[-1]
    
    
    def find_index(self, days, iter_id, week, month):
        week_id, month_id = iter_id, iter_id

        while True:
            # if iter_id == 4: 
            #     print('week',week_id,days[week_id],days[week_id] + week,days[iter_id])
            week_id -= 1
            if week_id == -1: break
            if days[week_id] + week <= days[iter_id]:
                # week_id+=1
                # print('llaal')
                break
                
        while True:
            month_id -= 1
            if month_id == -1: break
            if days[month_id] + month <= days[iter_id]:
                # month_id+=1
                break  

        return week_id, month_id
