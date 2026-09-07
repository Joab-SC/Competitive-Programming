"""
B. Evanescent
time limit per test2 seconds
memory limit per test256 megabytes
Let f(s)
 be the compressed version of a string s
, formed by replacing every maximal contiguous block of identical characters with a single copy of that character. For example, f(
"aabbcc") = 
"abc".

Let |s|
 denote the length of a string s
. Following this, |f(s)|
 denotes the length of the compressed string. For example:

|f(
"aabbcc")|=
 |
"abc"|
 =3
If the string is empty, its length is 0
.
Yousef has given you a string s
 consisting of n
 lowercase Latin letters. You must delete exactly one character si
 (2≤i≤n−1
) to form a new string s′
, and then find the minimum possible value of |f(s′)|
.

Note that you cannot delete s1
 or sn
.
"""

from itertools import groupby
def main():
    n = int(input())
    for _ in range(n):
        _ = input()
        s = input()
        s_list = list(s)
        remove_char(s_list)
        print(len(apply_func(''.join(s_list))))


def remove_char(str):
    posible_i = 1
    for i in range(1, len(str) - 1):
        if str[i-1] == str[i+1] != str[i]:
            del str[i]
            return 
        elif str[i-1] != str[i] and str[i+1] != str[i]:
            posible_i = i
    del str[posible_i]
    return
            
            
def apply_func(s):
    return ''.join([char for char, _ in groupby(s)])

            

        
main()