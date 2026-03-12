from collections import deque

def flood_fill(r: int, c: int, replacement: int, image: list[list[int]]) -> list[list[int]]:
    num_rows, num_cols = len(image), len(image[0])
    root_color = image[r][c]

    # same optimization as discussed: nothing to do if color doesn't change
    if root_color == replacement:
        return image

    def get_neighbors(i: int, j: int):
        # matrix-as-graph: 4-directional neighbors
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = i + di, j + dj
            # bounds + only traverse cells with the original/root color
            if 0 <= ni < num_rows and 0 <= nj < num_cols and image[ni][nj] == root_color:
                yield ni, nj

    # BFS template
    q = deque()
    q.append((r, c))

    # mark visited by recoloring immediately (alternative to a visited[][] array)
    image[r][c] = replacement

    while q:
        i, j = q.popleft()
        for ni, nj in get_neighbors(i, j):
            image[ni][nj] = replacement  # replace color (also marks visited)
            q.append((ni, nj))

    return image
