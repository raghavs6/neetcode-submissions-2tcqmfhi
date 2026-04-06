class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #we have an I and then we have an r that one ahead of i and then r and then add l 
        res = []
        nums.sort()

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue

        

            while l < r:
                total =  nums[i] + nums[r] + nums[l] 

                
            
                if total == 0:
                    res.append([nums[i], nums[r], nums[l]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                # Skip duplicates for right pointer
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
                    
                

        return res

                
