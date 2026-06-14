class Solution:
    def isHappy(self, n: int) -> bool:
        def square(num):
            result = 0
            while num > 0:
                rem = num % 10
                num //= 10
                result += rem * rem
            return result

        slow = square(n)
        fast = square(square(n))

        while slow != 1:
            if slow == fast:
                return False

            slow = square(slow)
            fast = square(square(fast))

        return True
