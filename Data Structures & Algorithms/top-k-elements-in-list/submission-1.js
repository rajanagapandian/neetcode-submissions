class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
  const count = {};

  for (const num of nums) count[num] = (count[num] || 0) + 1;

  const buckets = []
  for (const [k, v] of Object.entries(count)) {
    if (!buckets[v]) buckets[v] = []
    buckets[v].push(k)
  }
  const result = [];

  for (let i = nums.length; i > 0; --i) {
    if (!buckets[i]) continue;
    for (const num of buckets[i]) {
      result.push(num);
      if (result.length == k) {
        return result;
      }
    }
  }

  return result;
    }
}
