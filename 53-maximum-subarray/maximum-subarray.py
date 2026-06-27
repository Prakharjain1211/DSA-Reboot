class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bestending ,ans = nums[0],nums[0]
        for i in range(1,len(nums)):
            c1 = bestending + nums[i]
            c2 = nums[i]
            bestending = max(c1,c2)
            ans = max(ans,bestending)
        return ans