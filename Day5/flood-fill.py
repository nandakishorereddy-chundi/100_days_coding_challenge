class Solution:
    def is_valid(self, x, y, v, image):
        if x >= 0 and x < self.r and y >= 0 and y < self.c and v[x][y] != 1 and image[x][y] == self.orginial_color:
            return 1
        return 0

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        from collections import deque
        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]
        self.r = len(image)
        self.c = len(image[0])
        self.orginial_color = image[sr][sc]
        v = [[0 for j in range(self.c)] for i in range(self.r)]
        q = deque()
        q.append((sr, sc))
        while len(q) > 0:
            pos = q.popleft()
            x = pos[0]
            y = pos[1]
            v[x][y] = 1
            image[x][y] = color
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if self.is_valid(new_x, new_y, v, image):
                    q.append((new_x, new_y))
        return image