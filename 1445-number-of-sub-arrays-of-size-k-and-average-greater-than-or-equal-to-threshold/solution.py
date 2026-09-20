class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        
        no_of_subarray = len(arr) - k +1
        count = 0
        sum_window = sum(arr[0:k])
        count_subarray = 1
        i = 0

        while count_subarray <= no_of_subarray:
            
            if sum_window / k >= threshold:
                count +=1
            
            if i + k < len(arr):
                sum_window = sum_window - arr[i] + arr[i + k]
            
            i += 1  
            count_subarray += 1
        
        return count
