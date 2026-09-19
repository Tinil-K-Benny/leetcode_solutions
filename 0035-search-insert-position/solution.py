class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        idx = nums.index(target) if target in nums else -1

        if idx == -1:
            for i in range(len(nums)):
                if i == 0:
                    if nums[i] > target:
                        return 0
                if i == len(nums) - 1:
                    if nums[i] < target:
                        return i +1
                elif nums[i] < target and nums[i +1] > target:
                    return i +1
        
        else:
            return idx

                
        
