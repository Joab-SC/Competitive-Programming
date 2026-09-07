"""
Lola keeps a long to-do list of tasks she needs to finish. Each task has a difficulty number (the bigger the number, the harder the task), and the tasks must be completed in the order they appear.

The list keeps growing because items are rarely removed. Tired of that, Lola decided to take action: she wants to split her list into several consecutive groups of tasks, where each group represents the work she will do in one day.

To stay motivated, Lola wants to feel that each day is a step forward. So, starting from the second day, the hardest task of that day must be strictly harder than the hardest task from the previous day.

Lola also does not want to do too much in one day, so she wants to spread the work over as many days as possible.

What is the maximum number of days she can split the tasks into under these rules?
"""

def main():
    n = input()
    dif = list(map(int,input().split()))
    print(get_days(dif))

def get_days(arr):
    counter = 0
    actual = 0
    for i in arr:
        if i>actual:
            counter+=1
            actual = i
    return counter
main()