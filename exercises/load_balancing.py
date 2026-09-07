from math import ceil
def main():
    n, b = list(map(int, input().split()))
    xs =[]
    ys = []
    for _ in range(n):
       x, y = map(int, input().split()) 
       xs.append(x)
       ys.append(y)
    xodered = sorted(xs)
    yordered = sorted(ys)
    
    a = get_value(xodered)
    b = get_value(yordered)
    print(a)
    print(b)
        
    d = {1:0, 2:0, 3:0, 4:0}
    for i in range(n):
        if xs[i] < a and ys[i] <b:
            d[1]+= 1
        elif xs[i] < a and ys[i] >b:
            d[2]+= 1
        elif xs[i] > a and ys[i] >b:
            d[3]+= 1
        elif xs[i] > a and ys[i] <b:
            d[4]+= 1
    print(d)
    print(max(d.values()))
    
def get_value(l):
    posv = len(l)/2 -1
    v = -1
    if not posv.is_integer():
        if l[ceil(posv)] != l[ceil(posv)+1] != l[ceil(posv)-1]:
            v = l[ceil(posv)] + 1
        else:
            v1 = l[ceil(posv)] +1
            v2 = l[ceil(posv)] -1
            v1_count_left = len([x for x in l if x < v1])
            v1_count_right = len(l) - v1_count_left
            
            v2_count_left = len([x for x in l if x < v2])
            v2_count_right = len(l) - v2_count_left
            v = v1 if abs(v1_count_left - v1_count_right) < abs(v2_count_left - v2_count_right) else v2
        
    
    
    else:
        if l[posv] != l[posv+1]:
            v = (l[posv] +l[posv+1])/2  
        else:
            v1 = l[posv] +1
            v2 = l[posv] -1
            v1_count_left = len([x for x in l if x < v1])
            v1_count_right = len(l) - v1_count_left
            
            v2_count_left = len([x for x in l if x < v2])
            v2_count_right = len(l) - v2_count_left
            v = v1 if abs(v1_count_left - v1_count_right) < abs(v2_count_left - v2_count_right) else v2
    return v
            
    
main()
    