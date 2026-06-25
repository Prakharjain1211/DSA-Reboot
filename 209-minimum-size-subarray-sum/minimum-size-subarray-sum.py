class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        high,low,result,summ = 0,0,float('inf'),0
        while high < len(nums):
            summ = summ + nums[high]
            while(summ>=target):
                lengthofsubarray = high-low+1
                result = min(result,lengthofsubarray)
                summ = summ - nums[low]
                low+=1
            high+=1
        if result == float('inf'):
            return 0
        else:
            return result
        