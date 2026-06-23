class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        a = nums[0] + nums[1] + nums[2]
        for i in range(n - 2):            
            left, right = i + 1, n - 1            
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == target:                   
                    return current_sum

                if abs(current_sum-target) < abs (a-target):
                    a = current_sum

                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                    
        return a