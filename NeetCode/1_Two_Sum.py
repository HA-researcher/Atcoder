class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di={}
        for i,n in enumerate(nums):
            search=target-n
            if search in di:
                return [di[search],i]
            di[n]=i
        return []

        """
        list=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        """
