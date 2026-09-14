from math import gcd
def main():
    _ = input()
    numbers = list(map(int, input().split()))
    gcdsl = get_gcds_left(numbers)
    gcdsr =get_gcds_right(numbers)
    print(get_maximum(gcdsr, gcdsl, numbers))

def get_gcds_left(numbers):
    gcds = [0] * (len(numbers)+1)
    for i in range(len(numbers)):
        gcds[i+1] = gcd(gcds[i],numbers[i])
    gcds.append(0)
    return gcds
    
def get_gcds_right(numbers):
    gcds = [0] * (len(numbers)+2)
    for i in range(len(numbers)-1,-1,-1):
        gcds[i+1] = gcd(gcds[i+2],numbers[i])
    return gcds

def get_maximum(gcdsr, gcdsl, numbers):
    mx = gcdsr[1]
    for i in range(len(numbers)):
        mx = max(mx, gcd(gcdsl[i], gcdsr[i+2]))
    return mx
        
    
    
    
    

            
    """if len(numbers) <= 2:
            print(max(numbers))
            return
    
    inc = numbers.popleft()
    mx = reduce(gcd, numbers)
    numbers.append(inc)
    el = numbers.popleft()
    while(el != inc):
        mx = max(mx, reduce(gcd, numbers))
        numbers.append(el)
        el = numbers.popleft()
        
    print(mx)"""
    
    
    """mx = 1
    if len(numbers) == 2:
        print(max(numbers))
        return
    for el in numbers:
        ns = [x for x in numbers if x!= el]
        g = reduce(gcd,ns)
        mx = max(mx, g)
    print(mx)"""
    
main()