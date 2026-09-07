from itertools import chain
from collections import Counter

def main():
    n = int(input())
    for _ in range(n):
        s = list(input())
        r = get_minimum(s)
        print(r)
        
        
def get_minimum(s):
    counter = 0
    counter += s.count('4')
    s = [x for x in s if x!='4']
    l = []
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            n = int(s[i] + s[j])
            if n%4 == 0:
               l.append((i,j)) 
               
    fr = Counter(chain.from_iterable(l))
    while(len(l) != 0):
        mx = max(fr, key =lambda key:fr[key])
        counter += fr[mx]
        del fr[mx]
        
        for tpl in range(len(l) -1, 0, -1):
            if l[tpl][0] == mx or l[tpl][1] ==mx:
                del l[tpl]
    return counter
    
main()