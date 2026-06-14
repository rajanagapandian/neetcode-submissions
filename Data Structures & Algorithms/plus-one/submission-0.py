class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        result = (n+1) * [0]
        rem = 1

        for i in range(n, -1, -1):
            result[i] = digits[i-1] + rem
            rem = 0 if result[i] <= 9 else 1
            result[i] %= 10

        result[0] = rem if rem else 0
        
        return result if result[0] != 0 else result[1:]
