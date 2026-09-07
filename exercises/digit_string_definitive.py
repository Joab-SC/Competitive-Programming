def main():
    n = int(input())
    for _ in range(n):
        s = input()
        min =get_minimum(list(s))
        print(min)
        
        
def get_minimum(s):
    counter = 0
    counter += s.count('4')
    s = [x for x in s if x !='4']
    if len(s) == 0:
        return counter  
    
    l13 = [-1] * (len(s)+1)
    l13[0] = 0 
    for i in range(len(s)):
        if s[i] in ['1','3']:
            l13[i+1] = l13[i] + 1
        else:
            l13[i+1] = l13[i]
    
    l2 =[-1] * (len(s)+1)
    l2[-1] = 0 
    for i in range(len(s) - 1, -1, -1):
            if s[i] in ['2']:
                l2[i] = l2[i+1] + 1
            else:
                l2[i] = l2[i+1]
    
    
    l_min = 0
    l_min = l2[0]
    for i in range(len(s) + 1):
        onethree = l13[i]
        two = l2[i] 
        l_min = onethree + two if onethree +two<l_min else l_min
    return counter + l_min
main() 