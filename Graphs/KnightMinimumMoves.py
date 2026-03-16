# https://algo.monster/problems/knight_shortest_path
from collections import deque
def get_knight_shortest_path(x: int, y: int) -> int:    
    def get_neighbors (coord):
        res = []
        dirs = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        x,y = coord
        for dx,dy in dirs:
            nx = x + dx
            ny = y + dy
            res.append ((nx,ny))
        return res
                
    def bfs (start):
        queue = deque ([start]) # correct syntax
        visited = set ()
        steps = 0
        while len(queue) > 0:
            qSize = len (queue)
            for _ in range (qSize):
                node = queue.popleft()
                if node == (x,y):
                    return steps
                for nb in get_neighbors (node):
                    if nb in visited:
                        continue
                    queue.append (nb)
                    visited.add (nb)
            steps += 1
        return steps
    shortest_path = bfs ((0,0))    
    return shortest_path

if __name__ == "__main__":
    x = int(input())
    y = int(input())
    res = get_knight_shortest_path(x, y)
    print(res)
