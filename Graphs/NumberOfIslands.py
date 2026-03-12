from collections import deque 
def count_number_of_islands(grid: list[list[int]]) -> int:
    if grid is None or len (grid) == 0 or len (grid[0]) == 0:
        return 0
    rows = len (grid)
    cols = len (grid[0])
    visited = [[False for c in range(cols)] for r in range(rows)]  
    # get neighbors 
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]

    def bfs (sr, sc):        
        q = deque ([(sr,sc)])
        visited [sr][sc] = True    
        while len (q) > 0:
            x,y = q.popleft()
            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid [nx][ny] == 1:
                    visited [nx][ny] = True 
                    q.append ((nx,ny))            

    islands = 0
    for r in range (rows):
        for c in range (cols):
            if grid[r][c] == 1 and not visited [r][c]:
                islands +=1
                bfs (r,c)
    return islands

if __name__ == "__main__":
    grid = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = count_number_of_islands(grid)
    print(res)
