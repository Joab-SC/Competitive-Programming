"""
In a card game, there are n
 cards with values 2,3,4,…,n+1
.

To determine which of two cards with values x
 and y
 wins, apply the following rules:

if one of the numbers x
 and y
 is divisible by the other, the card with the smaller value wins;
otherwise, the card with the larger value wins.
For example, between cards 2
 and 6
, card 2
 wins because 6
 is divisible by 2
. Between cards 4
 and 6
, card 6
 wins because neither of these numbers is divisible by the other.

Determine whether there exists a card that wins against every other card.
"""
import math

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        if is_prime(n+1):
            print("YES")
        else:
            print("NO")
            

def is_prime(n):
    for i in range(2, math.ceil(n**0.5) +1):
        if n%i == 0:
            return False
    return True
main()