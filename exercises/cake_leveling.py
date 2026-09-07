"""
Alice is preparing a cake for her party. However, she is in a rush, so the frosting on the cake is uneven. To quickly solve this issue, Alice will put her knife at some integer height and then sweep the frosting from left to right to make the frosting level.

Formally, let ai
 be the height of the frosting at the i
-th position. Suppose that Alice puts her knife at some integer height h
. If the height of frosting at position i
 is greater than h
, the excess frosting will be pushed to position i+1
. Excess frosting on position n
 will be pushed off the cake completely.

Alice and her friends really love cake frosting. Since Alice might decide to serve some prefix of the cake instead of the whole cake, help her find the maximum height the frosting can be while keeping the frosting level for the first i
 positions for i=1,2,…,n

"""

def main():
    tot = int(input())
    for _ in range(tot): 
        _ = input()
        arr = list(map(int, input().split()))
        result = [arr[0]]
        extra = 0
        for i in range(1, len(arr)):
            num = arr[i]
            previous = result[i - 1]
            
            if num > previous:
                extra += num - previous
                result.append(previous)
            else: 
                extra += (previous - num) * len(result)
                to_distribute = extra//(len(result) + 1)
                extra = extra%(len(result) + 1)
                result.append(num + to_distribute)
        for num in result:
            print(num, end = " ")
        print()
main()