import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def main():
    n,m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    l, arr =get_minimum(graph,n)
    print(l)
    print(*arr)
    
def get_minimum(graph, ob):
    visited = set()
    parents = defaultdict(int)
    sons = deque()
    sons.append(1)
    parents[1] = 0
    visited.add(1)
    while sons:
        par = sons.popleft()
        if par==ob:
            break
        for el in graph[par]:
            if el in visited:
                continue
            visited.add(el)
            sons.append(el)
            parents[el] = par  
    path = []
    par = ob
    while par!=0:
        path.append(par)
        par = parents[par]
    path.reverse()
    return (len(path), path) 
main()