class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        Lmax = [0]*n
        Rmax = [0]*n
        ans = 0
        Lmax[0] = height[0]
        Rmax[n-1] = height[n-1]

        for i in range(1,n):
            Lmax[i] = max(Lmax[i-1],height[i])
        for i in range(n - 2, -1, -1):
            Rmax[i] = max(Rmax[i+1],height[i])
        for i in range(n):
            ans+= min(Lmax[i],Rmax[i])-height[i]
        return ans