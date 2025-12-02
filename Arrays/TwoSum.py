class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}
        for i,num in enumerate(nums):
            if target-num in di:                
                return [i,di[target-num]]
            else:
                di[num]= i
        return []           
        
