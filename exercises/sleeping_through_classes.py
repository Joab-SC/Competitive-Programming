def main():
    t = int(input())
    for _ in range(t):
        l, k = list(map(int, input().split()))
        s = list(map(int,input()))
        print(get_sleeping(s, k))

def get_sleeping(s, k):
    counter = 0
    counter_k = 0
    sleep = True
    for i in s:
        if i == 0 and sleep == True:
            counter += 1
            
        elif i == 1:
            sleep = False
            counter_k = 0
        
        elif i == 0 and sleep == False:
            counter_k += 1
        
        if k == counter_k:
            sleep =  True
    
            
    return counter
            
        
main()