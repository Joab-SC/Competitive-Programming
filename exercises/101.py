"""
The score of an array b
 of length m
 is defined as the maximum length of a subarray of b
 such that the first and last elements of the subarray are equal to 1
 and all other elements in the subarray are equal to 0
. Formally, the score of b
 is equal to the maximum integer k
 for which there exists an index i
 such that:

1≤i≤m−k+1
bi=bi+k−1=1
bi+1=bi+2=…=bi+k−2=0
If there is no subarray meeting the requirements, the score of b
 is 0
.

You are given an array a1,a2,…,an
, such that each element is equal to one of −1
, 0
, or 1
. Replace each −1
 with either a 0
 or 1
 such that the score of a
 is maximal over all possible ways to replace the −1
s in a
.

Input
The first line of each input contains t
 (1≤t≤104
) — the number of test cases.

The first line of each test case contains n
 (1≤n≤2⋅105
) — the length of a
.

The second line of each test case contains a1,a2,…,an
 (ai∈{−1,0,1}
) — the array a
.

It is guaranteed that the sum of n
 over all test cases does not exceed 2⋅105
.

Output
For each test case, output n
 space separated integers representing a
 after the −1
s were replaced with 0
s or 1
s. If there are multiple possible solutions, output any.

Example

"""
def main():
    t = int(input())
    for _ in range(t):
        n = input()
        s = list(map(int, input().split()))
        convert_min(s)
        print(" ".join(map(str, s)))
def convert_min(s):
    first1 = -1
    for i in range(len(s)):
        if s[i] ==  1:
            first1 = i
            break
        if s[i] == -1:
            s[i] = 1
            first1 =i
            break
        
    last1 = -1
    for i in range(len(s) -1, -1,-1):
        if s[i] ==  1:
            first1 = i
            break
        if s[i] == -1:
            s[i] = 1
            first1 =i
            break
    for i in range(len(s)):
        if i == first1 or i == last1:
            continue
        if s[i] == -1:
            s[i] = 0
main( )