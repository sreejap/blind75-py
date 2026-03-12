# use the template - bfs and get_neighbors, there is only one step to do to update the color
from collections import deque 
def flood_fill(r: int, c: int, replacement: int, image: list[list[int]]) -> list[list[int]]:
    def get_neighbors (cell,color):
        rows = len (image)
        cols = len (image[0])
        row, col = cell
        dir_x = [0,1,0,-1]
        dir_y = [1,0,-1,0]
        for i in range(len(dir_x)):
        #  for i in range len(dir_x): this is invalid syntax
            nb_x = row + dir_x[i]
            nb_y = col + dir_y[i]
            if 0 <=nb_x < rows and 0 <=nb_y < cols and image [nb_x][nb_y] == color:
                yield nb_x, nb_y        

    def bfs (root):
        # queue = deque [(root)] - incorrect syntax
        queue = deque ([root])
        r,c = root
        rows = len(image)
        cols = len(image[0])
        visited = [[False for c in range(cols)] for r in range(rows)]
        visited [r][c] = True
        color = image [r][c]
        image [r][c] = replacement
        while len(queue) >0:
            node = queue.popleft()
            for n in get_neighbors (node,color):
                nr, nc = n
                if visited [nr][nc]:
                    continue 
                visited[nr][nc] = True
                queue.append (n)
                image[nr][nc] = replacement
    bfs ((r,c))
    return image

if __name__ == "__main__":
    r = int(input())
    c = int(input())
    replacement = int(input())
    image = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = flood_fill(r, c, replacement, image)
    for row in res:
        print(" ".join(map(str, row)))
