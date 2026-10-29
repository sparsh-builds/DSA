# Given an array citations[] of size n such that citations[i] is the number of citations a researcher received for ith paper, find the H-index.

# H-index(H) is the largest value such that the researcher has published at least H papers that have been cited at least H times. <-

# 'H' stands for Hirsch index as it was proposed by the J.E. Hirsch in 2005. The H-index is defined as the author-level metric that attempts to measure both the productivity and the citation impact of the publication of the scientist or the scholar.

# Method 1 O(n*ogn) time complexity and O(1) space complexity   Comparison based sorting 


# [5,0,2,0,2]  -->  5,2,2,0,0

def hIndex(citations):
    
    # sort the citations in descending order
    citations.sort(reverse=True)
    n = len(citations)
    idx = 0

    # keep incrementing idx till citations[idx] > idx
    while idx < n and citations[idx] > idx:
        idx += 1
    return idx

if __name__ == '__main__':
    citations = [6, 0, 3, 5, 3]
    print(hIndex(citations))
    

# Method 2 Using Counting Sort O(n) time complexity and O(n) space complexity

# Counting sort 