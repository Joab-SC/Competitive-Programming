def main():
    t = int(input())
    for _ in range(t):
        _ = input()
        l = list(map(int, input().split()))
        one = l.count(1)
        cero = l.count(0)
        if one>=cero:
            print("Bessie")
        else:
            print("Elsie")
main()