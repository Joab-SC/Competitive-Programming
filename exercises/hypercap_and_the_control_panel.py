
from itertools import groupby
def main():
    t = int(input())
    for _ in range(t):
        _ = input()
        arr = list(map(int, input().split()))
        print(get_max(arr))
def get_max(arr):
    extra = 0
    total =0 
    for _,_ in groupby(arr):
        total +=1
    found = False    
        
    for i in range(len(arr)-3):
            if arr[i] == arr[i+1] and arr[i] !=arr[i+2] and arr[i]!=arr[i+3]:
                extra = 1
            if arr[i] == arr[i+1] and arr[i]!= arr[i+2] == arr[i+3]:
                extra = 2
                found = True
                break
    if not found:
        for i in range(len(arr)-1,2,-1):
                    if arr[i] == arr[i-1] and arr[i] !=arr[i-2] and arr[i]!=arr[i-3]:
                        extra = 1
                    if arr[i] == arr[i-1] and arr[i]!= arr[i-2] == arr[i-3]:
                        extra = 2
                        found = True
                        break
     
    if not found and len(arr)>=3:
        if arr[0] != arr[1] == arr[2]:
            extra= 1
        if arr[-1] != arr[-2] == arr[-3]:
            extra= 1
                    
    return total+extra
    
main()
