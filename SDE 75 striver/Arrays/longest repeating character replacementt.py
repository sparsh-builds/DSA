class Solution(object):
    def characterReplacement(self, s, k):
        
        n=len(s)

        

        replace=0

        max_length=0

        i=0
        j=0

        for i in range (n):

            freq=[0]*26

            max_freq=0


            for j in range (i,len(s)):

                freq[ord(s[j]) - ord('A')] += 1

                max_freq = max(max_freq, freq[ord(s[j]) - ord('A')])

                window_len = j - i + 1

                replace = window_len - max_freq

                # Check if we can replace within k
                if replace <= k:
                    max_length = max(max_length, window_len)
        return max_length



# uses SLiding window 

# 2 pointers approach

