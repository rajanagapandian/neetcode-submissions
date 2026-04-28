// index.ts
class Solution {
  encode(strs) {
    let result = "";
    for (const str of strs) {
      result += `${str.length}#${str}`;
    }
    return result;
  }
  decode(s) {
    const result = [];
    let i = 0;
    while (i < s.length) {
      const j = s.indexOf("#", i);
      const length = parseInt(s.substring(i, j));
      const str = s.substring(j + 1, j + 1 + length);
      result.push(str);
      i = j + 1 + length;
    }
    return result;
  }
}