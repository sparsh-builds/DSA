def check(s):
    
    left =0
    right =len(s)-1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True   # O (n) and O(1)

# using Atoi O(n) and O(1)

def myAtoi(s):
    i, n, sign, result = 0, len(s), 1, 0

    # skip leading whitespaces
    while i < n and s[i] == ' ':
        i += 1

    # handle optional sign
    if i < n and (s[i] == '+' or s[i] == '-'):
        sign = -1 if s[i] == '-' else 1
        i += 1

    # convert digits to integer
    while i < n and s[i].isdigit():
        digit = int(s[i])
        result = result * 10 + digit
        i += 1

    return sign * result

