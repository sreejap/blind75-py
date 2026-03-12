from collections import deque 
def flood_fill(r: int, c: int, replacement: int, image: list[list[int]]) -> list[list[int]]:
    n,m = len (image), len (image[0])
    curr = image [r][c]

    if curr == replacement:
        return image

    q = deque ()
    q.append((r,c))
    image [r][c] = replacement
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]

    while q:
        i,j = q.popleft()
        for dx, dy in dirs:
            ni, nj = i + dx, j+dy
            if 0 <= ni < n and 0<= nj < m and image [ni][nj] == curr:
                image[ni][nj] = replacement
                q.append ((ni,nj))        
    return image

if __name__ == "__main__":
    r = int(input())
    c = int(input())
    replacement = int(input())
    image = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = flood_fill(r, c, replacement, image)
    for row in res:
        print(" ".join(map(str, row)))
