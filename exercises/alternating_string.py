"""
Let us call a string 𝑡 alternating if for every 𝑖 from 1 to 𝑛−1, the condition 𝑡𝑖≠𝑡𝑖+1 holds.

You are given a string 𝑠 consisting only of the letters "a" and/or "b". You may perform the following operation on it at most once:

choose a substring 𝑠𝑙𝑠𝑙+1…𝑠𝑟 consisting of at least one character;
after choosing the substring, you may invert all letters in it, that is, change every "a" to "b" and every "b" to "a" (you are allowed to do it, but you don't have to do it);
reverse the chosen substring, that is, transform the string 𝑠1𝑠2…𝑠𝑙−1𝑠𝑙𝑠𝑙+1…𝑠𝑟𝑠𝑟+1…𝑠𝑛 into 𝑠1𝑠2…𝑠𝑙−1𝑠𝑟𝑠𝑟−1…𝑠𝑙𝑠𝑟+1…𝑠𝑛.
Note that when performing such an operation, you are not required to do the second step. For example, for the string 𝑠= "ababbab", after one operation you can obtain "abababa" by choosing the substring 𝑠5𝑠6𝑠7 and doing the second step, or "bababab" by choosing the substring 𝑠1𝑠2𝑠3𝑠4 and not doing the second step. However, you always have to perform the third step of the operation.

Your task is to determine whether it is possible to obtain any alternating string from the string 𝑠.

"""

def main():
    n = int(input())
    for i in range(n):
        str = input()
        print(define_alternating(str))

def define_alternating(str):
    counter = 0
    for i in range(len(str)-1):
        if str[i] == str[i+1]:
            counter +=1
    if counter >= 3:
        return "NO"
    else:
        return "YES"

main()