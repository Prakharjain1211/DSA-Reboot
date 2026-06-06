/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let x = 0;
    for(let i =1;i<nums.length;i++)
    {
        if(nums[x] < nums[i])
        x++;
        nums[x] = nums[i];
    }
    return x+1;
};