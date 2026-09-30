def main():
    t = int(input())
    for _ in range(t):
        n,m = map(int,(input().split()))
        if m>=n:
            print("NO")
            return
        narr = [("narr", x) for x in list(map(int, input().split()))]
        marr = [("marr", x) for x in list(map(int, input().split()))]
        print(is_equalable(narr, marr))
def is_equalable(narr,marr):
    complete = sorted((narr + marr), key= lambda el: el[1])
    i = 0
    j = len(complete) -1
    equalable = True
    saves = 0
    while(equalable):
        if i>j:
            break
        if complete[i][0] == "narr" == complete[j][0]:
            i+=1
            j-=1
            saves +=1
        elif complete[i][0] == "marr" == complete[j][0]:
            if i==j:
                saves-=1
            else:
                saves-= 2
            i+=1
            j-=1
            
        elif complete[i][0] == "marr":
            i+=1
            saves -=1
        elif complete[j][0] == "marr":
            j-=1
            saves -=1
            
        if saves <0:
            equalable = False
    return "YES" if equalable else "NO"

main()