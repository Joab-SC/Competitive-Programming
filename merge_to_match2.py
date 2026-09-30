def main():
    t = int(input())
    for _ in range(t):
        n,m = map(int,(input().split()))
        narr = sorted(list(map(int, input().split())))
        marr = sorted(list(map(int, input().split())))
        if not n>=2*m:
            print("NO")
            continue
        print(is_equalable(marr, narr))
def is_equalable(narr,marr):
    first = marr[0:(len(narr))]
    last = marr[len(marr)- len(narr): len(marr)]
    equalable = True
    for i in range(len(narr)):
        if not (first[i] <= narr[i] <= last[i]):
            equalable = False
            break
    return "YES" if equalable else "NO"

main()