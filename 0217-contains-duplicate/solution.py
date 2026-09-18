class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:


        return len(set(nums)) != len(nums)
        # s = set()

        # for i in nums:
        #     if i in s:
        #         return True
        #     else:
        #         s.add(i)
        
        # return False
