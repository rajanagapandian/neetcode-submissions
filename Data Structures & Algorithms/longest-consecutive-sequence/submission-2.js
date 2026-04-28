class Solution {
  /**
   * @param {number[]} nums
   * @return {number}
   */
  longestConsecutive(nums) {
    if (nums.length == 0) {
        return 0;
    }
    const unique = new Set(nums);
    let maxLength = 1;

    for (const num of nums) {
      if (unique.has(num - 1)) continue;
      let length = 1,
        data = num;
      while (unique.has(data + 1)) {
        data++;
        length++;
        maxLength = Math.max(maxLength, length);
      }
    }
    return maxLength;
  }
}