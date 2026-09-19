class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        max_avg = 0
        window_sum = 0

        for i in range (len(nums)):

            if i + k <= len(nums):
                
                if i == 0:
                    window_sum = sum(nums[i:i+k])
                    avg = window_sum
                    max_avg = avg

                else:
                    window_sum = window_sum - nums[i-1] + nums[i+k-1]
                    avg = window_sum
                    max_avg = max(max_avg, avg)

        return max_avg/k
                
            


        
