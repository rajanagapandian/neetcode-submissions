class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const indexMap = new Map();

        for (let i = 0; i < nums.length; ++i) {
            if (indexMap[target - nums[i]] !== undefined) return [indexMap[target-nums[i]], i];
            indexMap[nums[i]] = i;
        }

        return [];
    }
}
