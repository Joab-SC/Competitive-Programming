"""
Construct an array of 4⋅n
 integers such that:

each number 1,2,…,n
 appears in the array exactly 4
 times;
let px,i
 be the position of the i
-th occurrence of number x
 in the array; then, for each x
 from 1
 to n
, the numbers (px,2−px,1),(px,3−px,2),(px,4−px,3)
 must be pairwise distinct.
For example, for n=3
, one possible array is [1,1,2,1,2,3,1,3,2,2,3,3]
, because:

p1,2−p1,1=1,p1,3−p1,2=2,p1,4−p1,3=3
 — all numbers are distinct;
p2,2−p2,1=2,p2,3−p2,2=4,p2,4−p2,3=1
 — all numbers are distinct;
p3,2−p3,1=2,p3,3−p3,2=3,p3,4−p3,3=1
 — all numbers are distinct.
"""

def main():
    n = int(input())
    for _ in range(n):
        p = int(input())
        print(" ".join(map(str,create_sequence(p))))
def create_sequence(p):
    if p == 2:
        return [1,2,1,2,2,1,1,2]
    r1 = [0] * p
    r2 = r1
    r3 = r1[:]
    r4 = r1[:]
    for i in range(p):
        r1[i] = i+1
        r3[(i+1) % p] = i+1  
        r4[(i+3) % p]  = i+1
    return  r1 + r2 + r3 + r4
main()
