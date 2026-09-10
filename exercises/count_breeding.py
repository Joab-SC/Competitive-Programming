def main():
    n, q = list(map(int, input().split()))
    breeds = []
    for _ in range(n):
        breed = int(input())
        breeds.append(breed)
    prefix = prefix_breeds(breeds)
    for _ in range(q):
        a,b = list(map(int, input().split()))
        print(count_breeds(prefix, a, b))


def prefix_breeds(breeds):
    prefix = [(0,0,0)] * (len(breeds) + 1) 
    for i in range(len(breeds)):
        if breeds[i] == 1:
            a,b,c = prefix[i]
            prefix[i+1] = (a + 1, b, c)
        elif breeds[i] == 2:
            a,b,c = prefix[i]
            prefix[i+1] = (a, b + 1, c)
        else:
            a,b,c = prefix[i]
            prefix[i+1] = (a, b, c + 1)
    return prefix

def count_breeds(prefix, lim_inf, lim_sup):
    (a,b,c) = prefix[lim_sup]
    (d,e,f) = prefix[lim_inf - 1]
    return a - d , b - e, c - f
    
main()