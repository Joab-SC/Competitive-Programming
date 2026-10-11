from collections import defaultdict
import heapq
def main():
    src, n, ed = list(map(int, input().split()))
    graph = defaultdict(list)
    for i in range(ed):
        s,w,v = list(map(int, input().split()))
        graph[s].append((w,v))
    
    heap = []
    distances = [float('inf')]*(n+1)
    distances[src] = 0
    heapq.heappush(heap, (0,src))
    while heap:
        d,v = heapq.heappop(heap)
        if d < distances[v]:
            continue
        for w,u in graph[v]:
            newDist = d+w
            if newDist < distances[u]:
                distances[u] = newDist
                heapq.heappush(heap, (newDist, u))
                
    print(distances)
main()