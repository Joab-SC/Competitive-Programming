def main():
    n,k,c = list(map(int,input().split()))
    l = []
    
    for i in range(n):
        t,s = list(map(int, input().split()))
        l.append([t,s,0])
        
            
    total = 0
    counter = {}

    for i in range(len(l)):
        s = l[i][1]
        if s in counter:
            counter[s]+=1
        else:
            counter[s] = 1
        
        if counter[s]<=c and total < k:
            l[i][2] = 1
            total +=1
    

    i = 0
    while (k > total):
        if l[i][2] == 0:
            l[i][2] = 1
            total +=1
        i +=1
    
    for el in l:
        if el[2] == 1:
            print(el[0])
    
    
main()