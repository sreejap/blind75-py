from collections import deque 

def shortest_path(graph: list[list[int]], a: int, b: int) -> int:
    bfsQ = deque ([a])
    visited = [False]*len(graph)
    shortest_path = 0
    while len (bfsQ) > 0:
        n = len (bfsQ)
        for i in range (n):
            node = bfsQ.popleft()
            if node == b:
                return shortest_path            
            visited[node] = True
            for i in graph[node]:
                if not visited[i]:               
                    bfsQ.append(i)
        shortest_path += 1       
        
    return shortest_path

if __name__ == "__main__":
    graph = [[int(x) for x in input().split()] for _ in range(int(input()))]
    a = int(input())
    b = int(input())
    res = shortest_path(graph, a, b)
    print(res)
