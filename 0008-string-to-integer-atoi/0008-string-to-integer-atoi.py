class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        # Step 1: Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Check the sign
        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # Step 3: Convert digits to integer
        num = 0

        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            num = num * 10 + digit
            i += 1

        # Step 4: Apply the sign
        num *= sign

        # Step 5: Clamp to 32-bit integer range
        if num < INT_MIN:
            return INT_MIN

        if num > INT_MAX:
            return INT_MAX

        return num