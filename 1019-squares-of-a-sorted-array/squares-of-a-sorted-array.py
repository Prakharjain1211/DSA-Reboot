class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """        
        newarr =[]
        i=0;j=len(nums)-1

        while(i<=j):
            if(nums[i]**2 > nums[j]**2):
                newarr.insert(0, nums[i]**2)
                i+=1
            else:
                newarr.insert(0, nums[j]**2)
                j-=1
        return newarr