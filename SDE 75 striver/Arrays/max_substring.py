def lengthOfLongestSubstring(self, s: str) -> int:
    res = ""
    max_len = 0

    for char in s:
        if char in res:
            # Drop everything from the start up to and including the duplicate
            idx = res.index(char)
            res = res[idx + 1 :]

        res += char
        max_len = max(max_len, len(res))

    return max_len
def lengthOfLongestSubstring(self, s: str) -> int:
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        # Remove characters from the left until the duplicate is gone
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len

