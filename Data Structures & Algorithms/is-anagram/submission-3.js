class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length != t.length) return false;
      const count = new Map();

    for (const _s of s) count[_s] = (count[_s] || 0) + 1;

    for (const _t of t) {
        if (!count[_t] || count[_t] <= 0) return false;
        count[_t] = count[_t] - 1;
    }

    return true;
    }
}
