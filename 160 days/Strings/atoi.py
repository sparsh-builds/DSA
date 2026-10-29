#  Given a string s, convert it into a 32-bit signed integer (similar to the atoi() function) without using any built-in conversion functions.
# The conversion follows these rules:

# Ignore Leading Whitespaces: Skip all leading whitespace characters.
# Check Sign: If the next character is either '+' or '-', take it as the sign of the number. If no sign is present, assume the number is positive.
# Read Digits: Read the digits and ignore any leading zeros. Stop reading when a non-digit character is encountered or the end of the string is reached. If no digits are found, return 0.
# Handle Overflow: If the number exceeds the range of a 32-bit signed integer:
# Return 2³¹ − 1 (i.e., 2147483647) if it is greater than the maximum value.
# Return −2³¹ (i.e., -2147483648) if it is smaller than the minimum value.
# Return the final integer value.

# Examples:

# Input: s = "-123"
# Output: -123
# Explanation: It is possible to convert -123 into an integer so we returned in the form of an integer
# Input: s = " -"
# Output: 0
# Explanation: No digits are present, therefore the returned answer is 0.
# Input: s = " 1231231231311133"
# Output: 2147483647
# Explanation: The converted number will be greater than 231 – 1, therefore print 231 – 1 = 2147483647.
# Input: s = "-999999999999"
# Output: -2147483648
# Explanation: The converted number is smaller than -231, therefore print -231 = -2147483648.
# Input: s = "  -0012gfg4"
# Output: -12
# Explanation: Nothing is read after -12 as a non-digit character ‘g’ was encountered.
# Constraints:
# 1 ≤ |s| ≤ 15


# Iterative Approach - O(n) Time and O(1) Space
# Traverse the string from left to right, skipping whitespaces, handling the optional sign, and building the number digit by digit. At each step, ensure the value stays within 32-bit integer limits to avoid overflow.

# How to check if the number is greater than 231 - 1 or smaller than -231 ?

# The naive way is to use a data type larger than 32 bits like long or BigInteger to store the number. However, we can also use a 32-bit integer by appending the digits one-by-one and, for each digit, checking whether appending it will cause overflow.

# Since we construct the number as a positive value and apply the sign at the end, we only need to check against 231 - 1. While appending a digit to the current number, we can have 3 cases:
# Case 1: current number < (231 - 1)/10 then simply append the digit to the current number as it will not cause overflow.
# Case 2: current number > (231 - 1)/10 then return 231 - 1 in case of overflow.
# Case 3: current number = (231 - 1)/10 then in this case, only digits from 0 to 7 can be appended safely. If the next digit is greater than 7, return 231 - 1.

# Method 1 O(n) Time and O(1) Space

def myAtoi1(s):
    sign = 1
    res = 0
    idx = 0
    n = len(s)

    # Ignore leading whitespaces
    while idx < n and s[idx] == ' ':
        idx += 1

    # Store the sign of number
    if idx < n and (s[idx] == '+' or s[idx] == '-'):
        if s[idx] == '-':
            sign = -1
        idx += 1

    # Construct the number digit by digit
    while idx < n and '0' <= s[idx] <= '9':  # When idx = 6, s[6] is 'g'.

# ASCII value of 'g' is 103, while '9' is 57.
        digit = ord(s[idx]) - ord('0')  # ord calc ascii val of character
        res = 10 * res + digit

        # Handle overflow and underflow
        if res > 2**31 - 1:
            return (2**31 - 1) if sign == 1 else -2**31

        idx += 1

    return res * sign

# Recursive Approach - O(n) Time and O(n) Space
# Process the string recursively by skipping whitespaces, determining the sign, and building the number one digit at a time. At each recursive step, check for overflow and stop when a non-digit character is encountered or the string ends.

# Parse digits recursively with overflow handling
def parseDigits(s, idx, res, sign):
    if idx >= len(s) or s[idx] < '0' or s[idx] > '9':
        return res * sign

    digit = ord(s[idx]) - ord('0')

    if res > (2**31 - 1 - digit) // 10:
        return (2**31 - 1) if sign == 1 else -(2**31)  # Max Positive: $+2147483647$ (ends in 7)Min Negative: $-2147483648$ (ends in 8)

    return parseDigits(s, idx + 1, res * 10 + digit, sign)

def myAtoi(s):
    idx = 0

    # Skip leading spaces
    while idx < len(s) and s[idx] == ' ':
        idx += 1

    sign = 1

    # Handle sign
    if idx < len(s) and (s[idx] == '-' or s[idx] == '+'):
        if s[idx] == '-':
            sign = -1
        idx += 1

    return parseDigits(s, idx, 0, sign)

if __name__ == "__main__":
    print(myAtoi1(" -0012g4"))
    print(myAtoi(" -0012g4"))