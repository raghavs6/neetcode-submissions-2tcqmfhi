class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        n = len(nums)
        res = [1] * n
        
        # Pass 1: Calculate prefix products (everything to the left)
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        # Pass 2: Calculate suffix products (everything to the right)
        # and multiply them into the existing results
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res
                
            