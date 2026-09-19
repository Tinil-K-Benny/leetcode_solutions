class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        count = 0

        for i in range (len(nums)-1):
            if nums[i] < nums [i+1]:
                
                if count == 1 or count ==0:
                    count = 1
                elif count == 2 or count ==3:
                    count = 3
                else:
                    return False

            elif nums[i] > nums[i+1]:

                if count == 1 or count == 2:
                    count = 2
                else:
                    return False
            
            else:
                return False
            
        if count == 3:
            return True
        else:
            return False
