class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxending ,ans,minending = nums[0],nums[0],nums[0]
        for i in range(1,len(nums)):
            c1 = maxending * nums[i]
            c2 = nums[i]
            c3 = minending * nums[i]
            maxending = max(c1,c2,c3)
            minending = min(c1,c2,c3)
            ans = max(ans,maxending,minending)
        return ans