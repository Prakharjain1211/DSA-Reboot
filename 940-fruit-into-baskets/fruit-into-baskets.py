class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        low = 0
        result = float('-inf')
        occCounter = {}

        for high in range(len(fruits)):
            occCounter[fruits[high]] = occCounter.get(fruits[high], 0) + 1

            while len(occCounter) > 2:
                occCounter[fruits[low]] -= 1
                if occCounter[fruits[low]] == 0:
                    del occCounter[fruits[low]]  
                low += 1

            result = max(result, high-low+1)
        return result