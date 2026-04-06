class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}

        for nums in nums:
            if nums not in count:
                count[nums] = 1
            else:
                    count[nums] += 1
                    return True
        return False
            

