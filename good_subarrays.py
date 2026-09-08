"""
C. Good Subarrays
time limit per test2 seconds
memory limit per test256 megabytes
You are given an array a1,a2,…,an
 consisting of integers from 0
 to 9
. A subarray al,al+1,al+2,…,ar−1,ar
 is good if the sum of elements of this subarray is equal to the length of this subarray (∑i=lrai=r−l+1
).

For example, if a=[1,2,0]
, then there are 3
 good subarrays: a1…1=[1],a2…3=[2,0]
 and a1…3=[1,2,0]
.

Calculate the number of good subarrays of the array a
.

Input
The first line contains one integer t
 (1≤t≤1000
) — the number of test cases.

The first line of each test case contains one integer n
 (1≤n≤105
) — the length of the array a
.

The second line of each test case contains a string consisting of n
 decimal digits, where the i
-th digit is equal to the value of ai
.

It is guaranteed that the sum of n
 over all test cases does not exceed 105
.

Output
For each test case print one integer — the number of good subarrays of the array a


"""
from collections import Counter
def main():
    n = int(input())
    for _ in range(n):
        _ = input()
        t = [int(x)-1 for x in list(input())]
        prefix = [0]
        for i in range(len(t)):
            prefix.append(t[i] + prefix[i])
        prefix_map = dict(Counter(prefix))
        summ = 0
        for _, val in prefix_map.items():
            summ += sum(range(val))
        print(summ)
main()